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

## 7️⃣ Automatické připojování kontejnerů pomocí systemd

Pro pohodlné připojení kontejnerů po startu nebo ručně přes `systemctl`, vytvoř dva `systemd` jednotkové soubory pro šifrované kontejnery.

### a) `cryptsetup` jednotky

```bash
sudo nano /etc/crypttab
```

Přidej:

```
user1_backup /backup/container_user1.img none luks
user2_backup /backup/container_user2.img none luks
```

> ⚠️ `none` znamená ruční zadání hesla při připojování. Můžeš nahradit cestou ke klíči, např. `/etc/keys/user1.key`.

### b) Mount jednotky

Vytvoř mount jednotky, které se aktivují až po odemčení.

```bash
sudo nano /etc/systemd/system/mnt-user1_backup.mount
```

```ini
[Unit]
Description=Mount user1 backup container
Requires=dev-mapper-user1_backup.device
After=dev-mapper-user1_backup.device

[Mount]
What=/dev/mapper/user1_backup
Where=/mnt/user1_backup
Type=ext4
Options=defaults

[Install]
WantedBy=multi-user.target
```

Totéž pro `user2_backup`:

```bash
sudo nano /etc/systemd/system/mnt-user2_backup.mount
```

Potom:

```bash
sudo systemctl daemon-reexec
sudo systemctl daemon-reload
sudo systemctl enable mnt-user1_backup.mount
sudo systemctl enable mnt-user2_backup.mount
```

Připojení provedeno ručně (např. po rebootu):

```bash
sudo systemctl start mnt-user1_backup.mount
sudo systemctl start mnt-user2_backup.mount
```

---

## 8️⃣ Cron zálohování v noci

Naplánujeme denní noční zálohu v `crontab`. Např. ve 2:00 ráno.

### a) Rsync varianta

Spusť:

```bash
crontab -e
```

Přidej:

```
0 2 * * * /usr/local/bin/zalohuj_user1.sh
```

Vytvoř skript:

```bash
sudo nano /usr/local/bin/zalohuj_user1.sh
```

```bash
#!/bin/bash
cryptsetup luksOpen /backup/container_user1.img user1_backup
mount /dev/mapper/user1_backup /mnt/user1_backup
rsync -a --delete /data/ /mnt/user1_backup/
umount /mnt/user1_backup
cryptsetup luksClose user1_backup
```

Udělej spustitelný:

```bash
sudo chmod +x /usr/local/bin/zalohuj_user1.sh
```

Totéž můžeš udělat pro `user2`.

### b) BorgBackup varianta

Skript:

```bash
sudo nano /usr/local/bin/borg_zalohuj_user1.sh
```

```bash
#!/bin/bash
export BORG_REPO=/mnt/user1_backup
export BORG_PASSPHRASE='TVOJE_HESLO'  # nebo použij environment file

cryptsetup luksOpen /backup/container_user1.img user1_backup
mount /dev/mapper/user1_backup /mnt/user1_backup

borg create --compression zstd,5 --stats ::'{hostname}-{now:%Y-%m-%d}' /data

borg prune -v --keep-daily=7 --keep-weekly=4 --keep-monthly=6

umount /mnt/user1_backup
cryptsetup luksClose user1_backup
```

Přidáš opět do `crontab`:

```
0 2 * * * /usr/local/bin/borg_zalohuj_user1.sh
```

> ⚠️ Lepší zabezpečení: hesla uchovávej mimo skript, např. v `~/.borg-passphrase`.

---

## 🔐 Bonus: Použití klíčových souborů místo hesel

Místo ručního zadávání hesla můžeš pro LUKS použít klíč:

```bash
sudo dd if=/dev/urandom of=/etc/keys/user1.key bs=4096 count=1
sudo chmod 400 /etc/keys/user1.key
cryptsetup luksAddKey /backup/container_user1.img /etc/keys/user1.key
```

Pak aktualizuj `/etc/crypttab`:

```
user1_backup /backup/container_user1.img /etc/keys/user1.key luks
```

---

## 🧼 Úklid a testování

- Otestuj ručně: `sudo systemctl start mnt-user1_backup.mount`
- Otestuj cron job pomocí `sudo run-parts /etc/cron.daily/` nebo simuluj pomocí `at`.

---

## ✅ Celkový stav

- Systém běží z NVMe disku.
- Zálohy probíhají automaticky v noci.
- Jsou šifrované a bezpečné.
- Můžeš kdykoliv zálohovat ručně nebo automaticky.
- Přístup možný pouze z LAN (např. přes SSH).

