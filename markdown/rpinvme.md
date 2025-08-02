# 🛡️ Raspberry Pi 5: Přesun systému na NVMe + Šifrované zálohovací kontejnery

## 🧾 Cíl
- Přesunout systém ze SD karty na NVMe disk (Raspberry Pi 5).
- Nastavit dva šifrované kontejnery na NVMe disku pro zálohování (např. přes `rsync` nebo `borg`).
- Provoz pouze v rámci lokální sítě, dva uživatelé, přístup přes SSH.

---

## 1️⃣ Příprava

### Nutnosti:
- Raspberry Pi 5 s bootloaderem podporujícím NVMe.
- Funkční systém na SD kartě (`Raspberry Pi OS` doporučeno).
- NVMe disk správně rozpoznán (`lsblk` / `blkid`).
- Záloha systému před jakoukoliv operací (např. pomocí `rpi-clone` nebo `dd`).

---

## 2️⃣ Přesun systému na NVMe

### a) Zjisti zařízení

```bash
lsblk
```

SD karta bude např. `/dev/mmcblk0`, NVMe disk `/dev/nvme0n1`.

### b) Zkopíruj celý systém

```bash
sudo apt update && sudo apt install rsync
sudo mkdir /mnt/nvme
sudo mount /dev/nvme0n1p1 /mnt/nvme   # případně vytvoř oddíl + fs
sudo rsync -aAXv / /mnt/nvme --exclude={"/dev/*","/proc/*","/sys/*","/tmp/*","/run/*","/mnt/*","/media/*","/lost+found"}
```

### c) Aktualizuj `/mnt/nvme/etc/fstab`

Uprav záznamy podle nového UUID disku (`sudo blkid`).

```bash
UUID=xxxxxx / ext4 defaults,noatime 0 1
```

### d) Nastav boot z NVMe

Pokud máš nový bootloader (2023+), stačí odpojit SD kartu. Pokud ne:
- Nainstaluj `rpi-eeprom` a spusť `sudo raspi-config` > Advanced > Boot Order > NVMe.

---

## 3️⃣ Vytvoření šifrovaných kontejnerů

### a) Instalace potřebných balíčků

```bash
sudo apt install cryptsetup
```

### b) Vytvoření dvou šifrovaných souborů (např. 10 GB)

```bash
cd /backup

# Kontejner 1
fallocate -l 10G container_user1.img
cryptsetup luksFormat container_user1.img
cryptsetup luksOpen container_user1.img user1_backup
mkfs.ext4 /dev/mapper/user1_backup
mkdir /mnt/user1_backup
mount /dev/mapper/user1_backup /mnt/user1_backup

# Kontejner 2
fallocate -l 10G container_user2.img
cryptsetup luksFormat container_user2.img
cryptsetup luksOpen container_user2.img user2_backup
mkfs.ext4 /dev/mapper/user2_backup
mkdir /mnt/user2_backup
mount /dev/mapper/user2_backup /mnt/user2_backup
```

Po připojení:

```bash
# Přístup k nim přes mountpoint
/mnt/user1_backup
/mnt/user2_backup
```

### c) Zapsání automount skriptu (volitelně)

Vytvoř skript pro ruční připojení:

```bash
sudo nano /usr/local/bin/mount_backups.sh
```

```bash
#!/bin/bash
cryptsetup luksOpen /backup/container_user1.img user1_backup
mount /dev/mapper/user1_backup /mnt/user1_backup

cryptsetup luksOpen /backup/container_user2.img user2_backup
mount /dev/mapper/user2_backup /mnt/user2_backup
```

```bash
sudo chmod +x /usr/local/bin/mount_backups.sh
```

---

## 4️⃣ Nastavení zálohování

### Možnost A: Rsync přes SSH

Na klientu (např. pracovní stanice):

```bash
rsync -a --delete /data/ user@raspberrypi:/mnt/user1_backup/
```

### Možnost B: BorgBackup

Na RPi:

```bash
sudo apt install borgbackup
```

Na klientu:

```bash
borg init --encryption=repokey-blake2 user@raspberrypi:/mnt/user1_backup
borg create -v --stats ::{hostname}-{now:%Y-%m-%d} /data
```

---

## 5️⃣ Uživatelé a přístup

Přístup přes SSHFS nebo rsync přes SSH — není potřeba nic dalšího, stačí zajistit:
- Uživatel má přístup na `/mnt/userX_backup`.
- Autentizace klíčem, zamykání kontejnerů dle potřeby.

---

## 6️⃣ Zabezpečení

- LUKS šifrování — AES-XTS-PLAIN64, silné heslo nebo klíč.
- NVMe lze i plně zašifrovat (LUKS přes celý disk), ale zde je zvolen kontejner pro flexibilitu.
- Pravidelné zálohování `mount + rsync/borg` jako cronjob (spuštěno jen když mount existuje).

---

## ✅ Hotovo

Systém běží na NVMe, zálohování je šifrované, dostupné pouze přes LAN a chráněné pomocí LUKS.
