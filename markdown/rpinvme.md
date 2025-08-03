## 🛡️ Raspberry Pi 5: Přesun systému na NVMe + Šifrované zálohovací kontejnery

---

### 📢 Úvodní banner

> **Pozor:** Tento návod předpokládá základní znalost Linuxu, práce s terminálem a zálohování dat.  
> Před zahájením operací vždy proveď kompletní zálohu stávajícího systému.  
> Nesprávné použití může vést ke ztrátě dat!

---

### 📦 Seznam nutných balíčků

Instaluj je předem, pokud ještě nejsou:

```bash
sudo apt update
sudo apt install rsync cryptsetup borgbackup parted
```

---

### 1️⃣ Příprava

#### Nutnosti:
- Raspberry Pi 5 s bootloaderem podporujícím NVMe (většina po roce 2023).
- Funkční systém na SD kartě (`Raspberry Pi OS` 64bit doporučeno).
- NVMe disk fyzicky připojen a správně detekován (`lsblk`, `blkid`).
- Záloha systému před jakoukoliv operací: např. pomocí `rpi-clone`, `dd` nebo externí kopie na jiný disk.
- Počítej s potřebou jednoho restartu po změně diskových oddílů (kvůli informování kernelu).

---

### 2️⃣ Přesun systému na NVMe

#### a) Ověř připojení zařízení

```bash
lsblk
```

Hledej:
- SD karta = `/dev/mmcblk0`
- NVMe = `/dev/nvme0n1`

#### b) Vymaž a znovu vytvoř oddíly na NVMe

```bash
sudo umount /dev/nvme0n1*
sudo parted /dev/nvme0n1 mklabel gpt
sudo parted /dev/nvme0n1 mkpart primary ext4 0% 100%
sudo mkfs.ext4 /dev/nvme0n1p1
```

#### c) Připoj nový oddíl a zkopíruj systém

```bash
sudo mkdir /mnt/nvme
sudo mount /dev/nvme0n1p1 /mnt/nvme
sudo rsync -aAXv / /mnt/nvme --exclude={"/dev/*","/proc/*","/sys/*","/tmp/*","/run/*","/mnt/*","/media/*","/lost+found"}
```

#### d) Aktualizuj `fstab` v novém systému

Zjisti UUID:

```bash
sudo blkid
```

Pak uprav `/mnt/nvme/etc/fstab`:

```
UUID=XXXX-XXXX / ext4 defaults,noatime 0 1
```

#### e) Aktivuj boot z NVMe

Buď:
- Odpoj SD kartu a restartuj (funguje u nového bootloaderu),
nebo:
- Spusť `sudo raspi-config` > Advanced Options > Boot Order > NVMe
- Případně nainstaluj `rpi-eeprom` a zkontroluj firmware

---

### 3️⃣ Vytvoření šifrovaných zálohovacích kontejnerů

#### a) Instaluj `cryptsetup`

```bash
sudo apt install cryptsetup
```

#### b) Vytvoř šifrované soubory

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

#### c) Volitelný ruční mount skript

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

### 4️⃣ Zálohování

#### a) Rsync (klient → RPi)

```bash
rsync -a --delete /data/ user@raspberrypi:/mnt/user1_backup/
```

#### b) BorgBackup (moderní způsob)

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

### 5️⃣ Přístup uživatelů

- Přístup přes SSH.
- Uživatel má právo číst/zapisovat do `/mnt/userX_backup`.
- Používej klíčovou autentizaci.

---

### 6️⃣ Bezpečnost

- AES-XTS 512bit pomocí LUKS.
- Kontejnery = snadno přenositelné + flexibilní.
- Lze použít celý disk (LUKS přes `/dev/nvme0n1`), ale méně flexibilní.
- Doporučujeme zálohovat mimo RPi (např. NAS).

---

### 7️⃣ Automount přes systemd

#### a) crypttab

```bash
sudo nano /etc/crypttab
```

```
user1_backup /backup/container_user1.img none luks
user2_backup /backup/container_user2.img none luks
```

Pokud chceš použít klíčový soubor:

```bash
sudo mkdir -p /etc/keys
sudo dd if=/dev/urandom of=/etc/keys/user1.key bs=4096 count=1
sudo chmod 400 /etc/keys/user1.key
cryptsetup luksAddKey /backup/container_user1.img /etc/keys/user1.key
```

Pak do `crypttab`:

```
user1_backup /backup/container_user1.img /etc/keys/user1.key luks
```

#### b) mount jednotky

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

Totéž pro user2:

```bash
sudo nano /etc/systemd/system/mnt-user2_backup.mount
```

Aktivace:

```bash
sudo systemctl daemon-reexec
sudo systemctl daemon-reload
sudo systemctl enable mnt-user1_backup.mount
sudo systemctl enable mnt-user2_backup.mount
```

---

### 8️⃣ Cron noční zálohy

#### Rsync varianta

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

```bash
sudo chmod +x /usr/local/bin/zalohuj_user1.sh
crontab -e
```

```
0 2 * * * /usr/local/bin/zalohuj_user1.sh
```

#### BorgBackup varianta

```bash
sudo nano /usr/local/bin/borg_zalohuj_user1.sh
```

```bash
#!/bin/bash
export BORG_REPO=/mnt/user1_backup
export BORG_PASSPHRASE='TVE_HESLO'

cryptsetup luksOpen /backup/container_user1.img user1_backup
mount /dev/mapper/user1_backup /mnt/user1_backup

borg create --compression zstd,5 --stats ::'{hostname}-{now:%Y-%m-%d}' /data
borg prune -v --keep-daily=7 --keep-weekly=4 --keep-monthly=6

umount /mnt/user1_backup
cryptsetup luksClose user1_backup
```

Přidání do crontab:

```
0 2 * * * /usr/local/bin/borg_zalohuj_user1.sh
```

> ⚠️ Uchovávej hesla odděleně – např. `~/.borg-passphrase` s `chmod 600`.

---

### 🧼 Úklid & testování

- Testuj ruční mount: `sudo systemctl start mnt-user1_backup.mount`
- Testuj cron pomocí `sudo run-parts /etc/cron.daily/` nebo naplánuj `at now + 1 minute`
- Sleduj logy: `journalctl -xe`, `dmesg`, `systemctl status`

---

### 9️⃣ Časté problémy a řešení

#### Problém: NVMe disk není detekován nebo boot nefunguje  
- Zkontroluj, zda máš aktuální bootloader (příkaz `vcgencmd bootloader_version`) a firmware ([Raspberry Pi Documentation, 2024]).  
- Ujisti se, že NVMe disk je správně zapojený a napájený (některé NVMe vyžadují externí napájení).  
- Pokud nefunguje automatický boot, zkus bootovat ze SD a změnit boot order pomocí `raspi-config`.

#### Problém: Nelze připojit šifrovaný kontejner  
- Ověř heslo nebo klíčový soubor.  
- Zkontroluj, zda není kontejner poškozen (`cryptsetup luksDump container_user1.img`).  
- Pokud jsi použil klíčový soubor, ověř správnou cestu v `crypttab`.

#### Problém: Borg backup hlásí chybu přístupu  
- Zkontroluj práva přístupu ke složkám a správnost proměnných prostředí.  
- Heslo Borgu musí být správně nastaveno a dostupné během zálohy.

#### Problém: Cron joby neprobíhají správně  
- Podívej se do logů `journalctl -u cron` nebo `syslog`.  
- Cron nevidí některé proměnné prostředí – definuj je explicitně v skriptech.

---

### 🔗 Oficiální zdroje a další čtení

- Raspberry Pi Foundation (2024) *Bootloader and EEPROM*. Dostupné z: https://www.raspberrypi.com/documentation/computers/raspberry-pi.html#bootloader-and-eeprom [Cit. 2025-08-03].  
- Raspberry Pi OS Documentation (2024) *Using NVMe Storage*. Dostupné z: https://www.raspberrypi.com/documentation/computers/raspberry-pi.html#nvme-storage [Cit. 2025-08-03].  
- BorgBackup (2023) *Official Documentation*. Dostupné z: https://borgbackup.readthedocs.io/en/stable/ [Cit. 2025-08-03].  
- Cryptsetup (2023) *LUKS Disk Encryption*. Dostupné z: https://gitlab.com/cryptsetup/cryptsetup/-/wikis/Home [Cit. 2025-08-03].  
- Linux man pages (2025) *rsync(1), cryptsetup(8), systemd.mount(5)*. Dostupné z: https://man7.org/linux/man-pages/ [Cit. 2025-08-03].

---

### ✅ Celkový výsledek

- ✅ Systém běží z NVMe  
- ✅ Data zálohována denně a šifrovaně  
- ✅ Přístup přes SSH z LAN  
- ✅ Možnost použít i ruční zálohy  
- ✅ Bezpečné a snadno přenositelné kontejnery

