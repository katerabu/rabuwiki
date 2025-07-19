---
title: backupwin – zálohování z Win do RPi5
category: Počítače
tags: [linux, zalohovani, RPi, kyberbezpečnost]
last_update: 2025-07-19
---
# README: Šifrované zálohování ze dvou Windows 11 notebooků na Raspberry Pi 5 s NVMe 2TB 🔐💾🖥️

---

## Obsah 📚

1. [Přehled projektu](#přehled-projektu)  
2. [Hardware a síťové prostředí](#hardware-a-síťové-prostředí)  
3. [Požadavky a nástroje](#požadavky-a-nástroje)  
4. [Příprava Raspberry Pi 5 (Raspbian)](#příprava-raspberry-pi-5-raspbian)  
5. [Vytvoření a montování VeraCrypt kontejnerů](#vytvoření-a-montování-veracrypt-kontejnerů)  
6. [Nastavení Samba serveru](#nastavení-samba-serveru)  
7. [Nastavení SSH klíčů pro bezpečný přístup](#nastavení-ssh-klíčů-pro-bezpečný-přístup)  
8. [PowerShell zálohovací skripty pro Windows 11 + nastavení Plánovače úloh](#powershell-zálohovací-skripty-pro-windows-11--nastavení-plánovače-úloh)  
9. [Tipy a bezpečnostní doporučení](#tipy-a-bezpečnostní-doporučení)  
10. [Zdroje, citace a odkazy](#zdroje-citace-a-odkazy)  

---

## 1. Přehled projektu 📝

Zálohování dat ze dvou Windows 11 notebooků do šifrovaných VeraCrypt kontejnerů na Raspberry Pi 5 s NVMe diskem 2TB.  
Každý notebook má vlastní uživatelský účet a vlastní 512GB VeraCrypt kontejner.  
Data se přes Samba sdílení bezpečně přenášejí přes lokální intranet IPv4 subnet.  

---

## 2. Hardware a síťové prostředí 🖥️📡

- **Raspberry Pi 5** s NVMe SSD 2TB  
- OS: Raspbian (aktuální verze)  
- Síť: Intranet IPv4, jeden subnet (např. 192.168.1.0/24)  
- Dva Windows 11 notebooky, každý s vlastním uživatelem a heslem  

---

## 3. Požadavky a nástroje 🛠️

- VeraCrypt na Raspberry Pi  
- Samba server na Raspberry Pi  
- SSH server na Raspberry Pi  
- Windows 11 PowerShell na noteboocích  
- SSH klient (OpenSSH je v Windows 11 standardně dostupný)  

---

## 4. Příprava Raspberry Pi 5 (Raspbian) ⚙️🐧

### Aktualizace systému

    sudo apt update && sudo apt upgrade -y

### Instalace VeraCrypt, Samba, SSH

    sudo apt install veracrypt samba ssh -y

### Vytvoření uživatelských účtů pro Samba

    sudo adduser backupuser1
    sudo smbpasswd -a backupuser1

    sudo adduser backupuser2
    sudo smbpasswd -a backupuser2

---

## 5. Vytvoření a montování VeraCrypt kontejnerů 🔒

### Vytvoření 512 GB souborů kontejnerů

    dd if=/dev/zero of=/home/backupuser1/backupcontainer1.vc bs=1M count=524288
    dd if=/dev/zero of=/home/backupuser2/backupcontainer2.vc bs=1M count=524288

### Inicializace VeraCrypt kontejnerů

Pro uživatele `backupuser1`:

    veracrypt --text --create /home/backupuser1/backupcontainer1.vc \
      --size 512G --password=STRONG_PASSWORD1 --encryption=AES --hash=SHA-512 --filesystem=ext4

Pro uživatele `backupuser2`:

    veracrypt --text --create /home/backupuser2/backupcontainer2.vc \
      --size 512G --password=STRONG_PASSWORD2 --encryption=AES --hash=SHA-512 --filesystem=ext4

*(Zvolte silná a bezpečná hesla.)*

### Vytvoření mountpointů a montování

    sudo mkdir -p /mnt/backup1
    sudo mkdir -p /mnt/backup2

Montování kontejnerů:

    veracrypt --text --mount /home/backupuser1/backupcontainer1.vc /mnt/backup1 -p STRONG_PASSWORD1
    veracrypt --text --mount /home/backupuser2/backupcontainer2.vc /mnt/backup2 -p STRONG_PASSWORD2

---

## 6. Nastavení Samba serveru 🌐

### Úprava `/etc/samba/smb.conf`

Přidejte sekce:

    [Backup1]
       path = /mnt/backup1
       valid users = backupuser1
       read only = no
       browsable = yes

    [Backup2]
       path = /mnt/backup2
       valid users = backupuser2
       read only = no
       browsable = yes

### Restart Samba

    sudo systemctl restart smbd

---

## 7. Nastavení SSH klíčů 🔑

### Na Windows 11 notebooku v PowerShellu

Vygenerujte klíče (pokud ještě nejsou):

    ssh-keygen -t rsa -b 4096 -f $env:USERPROFILE\.ssh\id_rsa -N ""

### Přeneste veřejný klíč na Raspberry Pi (nahraďte IP a uživatele)

    scp $env:USERPROFILE\.ssh\id_rsa.pub backupuser1@192.168.1.X:/home/backupuser1/

### Na Raspberry Pi (pro backupuser1)

    mkdir -p /home/backupuser1/.ssh
    cat /home/backupuser1/id_rsa.pub >> /home/backupuser1/.ssh/authorized_keys
    chmod 700 /home/backupuser1/.ssh
    chmod 600 /home/backupuser1/.ssh/authorized_keys
    rm /home/backupuser1/id_rsa.pub

*Totéž opakujte pro `backupuser2` a druhý notebook.*

---

## 8. PowerShell zálohovací skripty pro Windows 11 + nastavení Plánovače úloh ⏰🖥️

### Notebook 1 – `BackupToRPi_User1.ps1`

    # PowerShell skript pro zálohu na Raspberry Pi Samba share Backup1

    $RPiIP = "192.168.1.X"                      # IP RPi
    $sharePath = "\\$RPiIP\Backup1"
    $backupSource = "C:\DataToBackup"           # Zdroj zálohy
    $timestamp = Get-Date -Format "yyyyMMdd_HHmmss"
    $backupDest = "$sharePath\Backup_$timestamp"

    # Připojení Samba sdílení pod písmenem Z:
    New-PSDrive -Name "Z" -PSProvider FileSystem -Root $sharePath -Persist

    # Vytvoření cílové složky na síťovém disku
    New-Item -ItemType Directory -Path $backupDest -Force | Out-Null

    # Kopírování dat
    Copy-Item -Path "$backupSource\*" -Destination $backupDest -Recurse -Force

    # Odpojení síťové jednotky
    Remove-PSDrive -Name "Z"

---

### Notebook 2 – `BackupToRPi_User2.ps1`

    # PowerShell skript pro zálohu na Raspberry Pi Samba share Backup2

    $RPiIP = "192.168.1.X"                      # IP RPi
    $sharePath = "\\$RPiIP\Backup2"
    $backupSource = "D:\WorkFiles"               # Zdroj zálohy
    $timestamp = Get-Date -Format "yyyyMMdd_HHmmss"
    $backupDest = "$sharePath\Backup_$timestamp"

    New-PSDrive -Name "Z" -PSProvider FileSystem -Root $sharePath -Persist
    New-Item -ItemType Directory -Path $backupDest -Force | Out-Null
    Copy-Item -Path "$backupSource\*" -Destination $backupDest -Recurse -Force
    Remove-PSDrive -Name "Z"

---

### Nastavení Plánovače úloh na Windows 11 📅

1. Otevřete **Plánovač úloh** (Task Scheduler).  
2. Vytvořte novou úlohu:  
   - Název: `Záloha na RPi BackupUser1` (resp. `BackupUser2`)  
   - Spouštění: Např. každý den v 19:00 nebo podle potřeby  
3. Akce:  
   - Spustit program: `powershell.exe`  
   - Argumenty: `-File "C:\Cesta\k\souboru\BackupToRPi_User1.ps1"` (resp. User2)  
4. V záložce **Obecné** zaškrtněte "Spustit s nejvyššími oprávněními"  
5. Uložte úlohu.  

---

## 9. Tipy a bezpečnostní doporučení ⚠️🔒

- Každý uživatel má vlastní VeraCrypt kontejner a Samba účet s oddělenými právy.  
- Uchovávejte silná a bezpečná hesla, ideálně spravujte v password manageru.  
- Raspberry Pi pravidelně aktualizujte (`sudo apt update && sudo apt upgrade`).  
- Omezte přístup v síti (firewall) na potřebné IP adresy.  
- Pravidelně testujte obnovu dat ze záloh.  
- Zálohujte i VeraCrypt kontejnery samotné (externí záloha).  
- Používejte SSH klíče místo hesel pro lepší bezpečnost.  
- Přemýšlejte o monitoringu Raspberry Pi a Samba serveru.  

---

## 10. Zdroje, citace a odkazy 📖🌐

- [VeraCrypt Official](https://www.veracrypt.fr/en/Home.html)  
- [Samba Documentation](https://www.samba.org/samba/docs/current/man-html/smb.conf.5.html)  
- [Microsoft Docs: Task Scheduler](https://learn.microsoft.com/en-us/windows/win32/taskschd/task-scheduler-start-page)  
- [Windows PowerShell Docs](https://learn.microsoft.com/en-us/powershell/)  
- [SSH Keygen on Windows](https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_keymanagement)  
- [Raspberry Pi OS Documentation](https://www.raspberrypi.com/documentation/computers/)  

---

Konec navodu! 🚀😊  
