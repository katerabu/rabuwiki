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


Jak dal pokracovat ->> mozne promprty pro AI:

A) autounmount vse s radnymi komentari hlavne co jaka metoda presne dela a proc
#!/bin/bash

#!/bin/bash

# ==== KONFIGURACE ====

# Cesta ke sifrovanemu LUKS kontejneru
CONTAINER_IMG="/home/liko/backup/container_liko.img"

# Kam se kontejner pripoji (mount point)
MOUNT_POINT="/mnt/liko_backup"

# Jmeno mapperu (jak bude dostupny pres /dev/mapper/)
MAPPER_NAME="liko_backup"

# Maximalni doba cekani na ukonceni aktivity (napr. 2 hodiny = 7200 sekund)
MAX_WAIT=7200

# Interval mezi kontrolami, zda kontejner nekdo pouziva (v sekundach)
CHECK_INTERVAL=30

# Promenna, do ktere se bude scitat cas cekani
ELAPSED=0

# ==== FUNKCE ====

# Funkce pro zobrazeni aktualniho casu (v logu u kazde zpravy)
timestamp() {
  date +"%Y-%m-%d %H:%M:%S"
}

# ==== START ====

echo "[$(timestamp)] [INFO] Sleduji aktivitu v $MOUNT_POINT..."
echo "[$(timestamp)] [INFO] Skript ukonci mount a zamkne kontejner, az nebude nikdo pracovat s daty."

# Nekonecny cyklus – sleduje aktivitu v mount pointu
while true; do

  # Kontrola, zda nekdo pracuje se soubory uvnitr mount pointu
  # `lsof +D` vypise vsechny otevrene soubory v dane slozce
  if sudo lsof +D "$MOUNT_POINT" > /dev/null 2>&1; then
    echo "[$(timestamp)] [WAIT] Kontejner stale pouzivan – aktivni. Dalsi kontrola za $CHECK_INTERVAL s..."
    sleep "$CHECK_INTERVAL"
    ELAPSED=$((ELAPSED + CHECK_INTERVAL))

    # Pokud jsme cekali dele nez MAX_WAIT, skript se ukonci
    if [ "$ELAPSED" -ge "$MAX_WAIT" ]; then
      echo "[$(timestamp)] [WARN] Maximalni cekani $MAX_WAIT s bylo prekroceno. Skript se ukoncuje."
      exit 1
    fi

  else
    # Pokud neni zadna aktivita, pokusime se kontejner odpojit a zamknout
    echo "[$(timestamp)] [INFO] Aktivita ustala. Pokousim se odpojit a zamknout..."

    # Pokus o odpojeni mount pointu
    if sudo umount "$MOUNT_POINT"; then
      echo "[$(timestamp)] [OK] Filesystem odpojen."

      # Pokud odpojeni probehne uspesne, pokusime se zavrit sifrovany kontejner
      if sudo cryptsetup luksClose "$MAPPER_NAME"; then
        echo "[$(timestamp)] [OK] Kontejner zamcen. Hotovo."
        exit 0
      else
        echo "[$(timestamp)] [ERR] Chyba pri zamykani kontejneru!"
        exit 2
      fi

    else
      # Pokud nelze odpojit (napr. soubor je stale otevreny), cekame a zkusime znovu
      echo "[$(timestamp)] [ERR] Odpojeni selhalo! Zkusim znovu za $CHECK_INTERVAL s..."
      sleep "$CHECK_INTERVAL"
    fi
  fi
done


B) spusteni jako systemd sluzba

spusteni jako systemd sluzba?
systemd je init system a spravce sluzeb v modernich Linuxech (v Raspbianu a vetsine distribuci je to systemd). Umoznuje automaticky spoustet skripty/sluzby pri startu systemu, sledovat je, znovu je spoustet, nebo je zastavit.

Systemd sluzba je konfiguracni soubor, ktery popisuje, jak a kdy se ma neco spustit.

Vyhody:

automaticke spousteni pri startu RPi

snadna sprava (start/stop/status)

systemd pohlida, aby se sluzba nezasekla, a muze ji znovu spustit

Priklad systemd sluzby pro tvuj backup skript:

/etc/systemd/system/backup-watch.service

ini
Zkopírovat
Upravit
[Unit]
Description=Automaticke odpojeni a zamknuti sifrovaneho backup kontejneru

[Service]
Type=simple
ExecStart=/home/liko/auto_unmount_backup.sh
Restart=on-failure
User=liko

[Install]
WantedBy=multi-user.target
Pak:

bash
Zkopírovat
Upravit
sudo systemctl daemon-reload
sudo systemctl enable backup-watch.service
sudo systemctl start backup-watch.service

Takhle se skript spusti pri startu a bezi na pozadi.

C) podporu pro vic kontejneru - klidne at zjisti jake kde jsou kontejnery a da na vyber - a pokud je uzamceny tak da na vyber odemceni

Podpora pro vic kontejneru a interaktivni vyber
Idea: Skript automaticky vyhleda vsechny .img soubory v adresari /home/liko/backup/, nabidne uzivateli, co chce:

pokud je kontejner odemceny a pripojen, nabidne ho odpojit a zamknout

pokud je kontejner zamceny (uzavreny), nabidne ho odemknout a pripojit

Navrh skriptu
najde vsechny kontejnery (napr. container_*.img)

zjisti, jestli jsou pres cryptsetup status <mapper_name> odemceny

dle stavu nabidne menu (pomoci select v bash)

podle volby odemkne/pripoji nebo odpoji/zamkne

Ukazkovy skript (hodne zjednoduseny, bez pokrocilych kontrol):

#!/bin/bash

BACKUP_DIR="/home/liko/backup"
MOUNT_BASE="/mnt"

# Funkce pro zobrazeni casu v logu
timestamp() {
  date +"%Y-%m-%d %H:%M:%S"
}

# Najdeme vsechny kontejnery .img
containers=($(ls "$BACKUP_DIR"/container_*.img 2>/dev/null))

if [ ${#containers[@]} -eq 0 ]; then
  echo "[$(timestamp)] [ERR] Neni nalezen zadny kontejner v $BACKUP_DIR"
  exit 1
fi

echo "Vyberte kontejner:"

select container_path in "${containers[@]}" "Konec"; do
  if [ "$container_path" == "Konec" ]; then
    echo "Konec vyberu."
    exit 0
  elif [ -n "$container_path" ]; then
    container_name=$(basename "$container_path" .img)
    mapper_name="${container_name}_backup"
    mount_point="$MOUNT_BASE/${container_name}_backup"

    # Zjistime stav kontejneru (odkryty nebo ne)
    if sudo cryptsetup status "$mapper_name" &>/dev/null; then
      status="opened"
    else
      status="closed"
    fi

    echo "Konainer '$container_name' je $status."

    if [ "$status" == "closed" ]; then
      # Odemknuti + mount
      echo "Odemknuti a pripojeni kontejneru..."

      sudo cryptsetup luksOpen "$container_path" "$mapper_name" || {
        echo "Chyba pri odemykani kontejneru"
        exit 1
      }

      sudo mkdir -p "$mount_point"

      sudo mount "/dev/mapper/$mapper_name" "$mount_point" || {
        echo "Chyba pri mountovani"
        sudo cryptsetup luksClose "$mapper_name"
        exit 1
      }

      sudo chown liko:liko "$mount_point"

      echo "Konainer odemcen a pripojen na $mount_point."

    else
      # Odpojeni + zamknuti
      echo "Odpojuji a zamykam kontejner..."

      sudo umount "$mount_point" || {
        echo "Chyba pri odpojeni mountpointu"
        exit 1
      }

      sudo cryptsetup luksClose "$mapper_name" || {
        echo "Chyba pri zamykani kontejneru"
        exit 1
      }

      echo "Konainer odpojen a zamcen."
    fi

    break
  else
    echo "Neplatna volba, zkuste to prosim znovu."
  fi
done
D) USERCASE po spusteni scriptu: list nalezenych kontejneru a jejich stav, nabidnout odemceni uzamcenych s tim, ze musi zacit kopirovat do nebo z nej do 30 sekund jinak automaticky uzavira... 
Jasne, to je super usercase — kombinuje interaktivitu i automatizaci. Tady je, jak bych to viděl krok po kroku:

Usecase:
Skript spustíš — automaticky najde všechny kontejnery (např. container_*.img).

Ukáže ti list kontejnerů s jejich stavem (opened/closed).

Ty vybereš kontejner, co chceš odemknout, nebo se připojit/odpojit.

Pokud je kontejner zamčený, po odemčení se spustí 30 sekundová doba, během které bys měl začít kopírovat data (třeba přes sshfs, scp nebo jinak).

Pokud do 30 sekund nedojde k žádné aktivitě v připojeném mountpointu, kontejner se automaticky zamkne a odpojí — aby zbytečně nezůstal otevřený.

Pokud aktivita probíhá, skript to pozná a bude čekat, dokud aktivita neskončí — pak taky bezpečně odpojí a zamkne.

Co všechno to bude potřebovat:
Skenování kontejnerů

Zjištění jejich stavu (cryptsetup status)

Interaktivní výběr (bash select)

Funkci na odemknutí/mount

Funkci na sledování aktivity (lsof +D nebo inotifywait)

Časovač pro 30s “startovací okno” pro aktivitu

Bezpečné odpojení a zamčení

Mám pro tebe základní prototyp s komentáři a funkcemi, co to dělají:

#!/bin/bash

BACKUP_DIR="/home/liko/backup"
MOUNT_BASE="/mnt"
IDLE_LIMIT=30  # cekani 30s na start aktivity po odemceni

timestamp() {
  date +"%Y-%m-%d %H:%M:%S"
}

# Zkontroluje, jestli je kontejner otevren
is_opened() {
  sudo cryptsetup status "$1" &>/dev/null
  return $?
}

# Odemkne a pripoji kontejner
unlock_and_mount() {
  local container_path="$1"
  local mapper_name="$2"
  local mount_point="$3"

  echo "[$(timestamp)] Odemykam kontejner $mapper_name..."
  sudo cryptsetup luksOpen "$container_path" "$mapper_name" || {
    echo "Chyba pri odemykani!"
    return 1
  }

  sudo mkdir -p "$mount_point"

  echo "[$(timestamp)] Pripojuji filesystem..."
  sudo mount "/dev/mapper/$mapper_name" "$mount_point" || {
    echo "Chyba pri mountovani!"
    sudo cryptsetup luksClose "$mapper_name"
    return 2
  }

  sudo chown liko:liko "$mount_point"
  echo "[$(timestamp)] Kontejner odemcen a pripojen na $mount_point."
  return 0
}

# Odpoji a zamkne kontejner
unmount_and_lock() {
  local mapper_name="$1"
  local mount_point="$2"

  echo "[$(timestamp)] Odpojuji $mount_point..."
  sudo umount "$mount_point" || {
    echo "Chyba pri odpojeni mountpointu."
    return 1
  }

  echo "[$(timestamp)] Zamykam kontejner $mapper_name..."
  sudo cryptsetup luksClose "$mapper_name" || {
    echo "Chyba pri zamykani kontejneru."
    return 2
  }

  echo "[$(timestamp)] Kontejner odpojen a zamcen."
  return 0
}

# Sledovani aktivity v mountpointu, vraci 0, kdyz je aktivita, jinak 1
wait_for_activity() {
  local mount_point="$1"
  local timeout="$2"
  local interval=3
  local elapsed=0

  echo "[$(timestamp)] Cekam na aktivitu v $mount_point po dobu $timeout sekund..."

  while (( elapsed < timeout )); do
    if sudo lsof +D "$mount_point" > /dev/null 2>&1; then
      echo "[$(timestamp)] Aktivita detekovana!"
      return 0
    fi
    sleep $interval
    ((elapsed+=interval))
  done

  echo "[$(timestamp)] Aktivita neprobehla."
  return 1
}

# Hlavni skript

containers=($(ls "$BACKUP_DIR"/container_*.img 2>/dev/null))

if [ ${#containers[@]} -eq 0 ]; then
  echo "[$(timestamp)] [ERR] Neni nalezen zadny kontejner v $BACKUP_DIR"
  exit 1
fi

echo "Vyberte kontejner:"

select container_path in "${containers[@]}" "Konec"; do
  if [ "$container_path" == "Konec" ]; then
    echo "Konec vyberu."
    exit 0
  elif [ -n "$container_path" ]; then
    container_name=$(basename "$container_path" .img)
    mapper_name="${container_name}_backup"
    mount_point="$MOUNT_BASE/${container_name}_backup"

    if is_opened "$mapper_name"; then
      echo "[$(timestamp)] Kontejner '$container_name' je odemceny."
      read -p "Chcete ho odpojit a zamknout? (a/n) " yn
      if [[ "$yn" =~ ^[Yy]$ ]]; then
        unmount_and_lock "$mapper_name" "$mount_point"
      else
        echo "Akce zrusena."
      fi
    else
      echo "[$(timestamp)] Kontejner '$container_name' je zamceny."
      read -p "Chcete ho odemknout a pripojit? (a/n) " yn
      if [[ "$yn" =~ ^[Yy]$ ]]; then
        if unlock_and_mount "$container_path" "$mapper_name" "$mount_point"; then
          if wait_for_activity "$mount_point" $IDLE_LIMIT; then
            echo "[$(timestamp)] Sledovani aktivity, cekam nez aktivita skonci..."
            # Tady muzeme pridat dalsi cekani na ukonceni aktivity nebo dalsi logiku
            echo "Prozatim skoncime."
          else
            echo "[$(timestamp)] Zadne kopirovani neprobehlo, automaticky zamykam."
            unmount_and_lock "$mapper_name" "$mount_point"
          fi
        else
          echo "Chyba pri odemykani a pripajeni."
        fi
      else
        echo "Akce zrusena."
      fi
    fi
    break
  else
    echo "Neplatna volba, zkuste to prosim znovu."
  fi
done
Jak to funguje:

Po spusteni ti vypise vsechny kontejnery.

Pokud je kontejner zamceny, umozni ho odemknout a pripojit.

Po odemceni ceká 30s, jestli zacnes nejakou aktivitu (napr. kopirovani).

Pokud ano, muzeme to prozatim ukoncit (do budoucna muzeme pridat dalsi cekani, aby to automaticky odpojilo po ukonceni prace).

Pokud ne, kontejner se zamkne automaticky.

Pokud je kontejner uz odemceny, nabidne se moznost ho zamknout.

Co rikas? Chces, abych to jeste dopracoval treba o dlouhodobe sledovani aktivity, nebo rovnou systemd integraci?

hmm to by slo, me jeste napadlo ze si bude malina tahat data k sobe sama, napriklad z win11 nejakeho backup adresare (samba asi neni moc bezpecna ale co uz jineho na windows) do kontejneru a druhy user pres sshfs z linux masiny nejaky backup adresar....

To je fakt fajn nápad — Malina si automaticky tahá zálohy z Windows (třeba přes SMB/Samba) a zároveň jiný uživatel může přes SSHFS přistupovat z Linuxu a zálohy taky ukládat přímo do šifrovaného kontejneru.

### Když to rozepisu podrobněji:

## 1) Tahání dat z Windows do Raspberry (maliny)
Pro Windows sdílení (Samba)

Nastavit na Windows sdílenou složku s uživatelem + heslem.

Na Raspberry připojit sdílenou složku přes mount.cifs s šifrovaným kontejnerem připojeným jako target pro zálohy.

Malina může mít skript, co třeba jednou denně připojí ten SMB share, zkopíruje nové soubory do kontejneru a zase odpojí.

Bezpečnost

Připojení přes CIFS není šifrované, ale SMB3 už má šifrování na protokolové úrovni, takže pokud je vše aktuální, je to OK.

Další možnost je přes VPN — aby byl SMB provoz uvnitř privátní sítě.

## 2) SSHFS přístup pro jiného uživatele (např. z Linux klienta)
Přes SSHFS připojí /mnt/liko_backup (kontejner) jako virtuální disk.

Bude to šifrované díky LUKS, takže data na disku jsou bezpečně uložena.

## 3) Jak to dát dohromady
Na Raspberry:

Automatický skript, co:

Odemkne kontejner (případně na požádání, nebo podle plánu).

Připojí kontejner k /mnt/liko_backup.

Připojí SMB share z Windows (např. do /mnt/windows_backup).

Spustí synchronizaci (např. rsync nebo cp).

Odpojí SMB share a kontejner bezpečně zamkne, pokud je neaktivní.

Současně může běžet sshd na Raspberry pro připojení jiných uživatelů přes SSHFS.

## 4) Několik tipů jak to zabezpečit
Na Windows používat silné heslo pro SMB share.

Využít firewall na Raspberry a Windows, aby SMB port nebyl přístupný z internetu.

Pokud je Raspberry na veřejné síti, zvážit VPN mezi Windows a Raspberry.

Uchovávat LUKS passphrase mimo Raspberry (např. ručně zadávat nebo v bezpečném hardware tokenu).

## 5) Ukázkový mini-plán pro skript na Raspberry (pseudo):

#!/bin/bash

# Odemknout kontejner
./unlock_container.sh

# Připojit SMB share z Windows
sudo mount.cifs //WIN_IP/backup /mnt/windows_backup -o user=winuser,password=winpass

# Synchronizace do kontejneru
rsync -av --delete /mnt/windows_backup/ /mnt/liko_backup/

# Odpojit SMB
sudo umount /mnt/windows_backup

# Bezpečně odpojit a zamknout kontejner
./auto_unmount_backup.sh


Závěr
Záloha z Windows na Raspberry v šifrovaném kontejneru — bezpečné a pohodlné.
Přístup přes SSHFS pro další uživatele.
Můžeš to celé automatizovat, sledovat aktivitu a bezpečně zamykat.


