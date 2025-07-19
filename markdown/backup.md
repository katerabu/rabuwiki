---
title: backup – zálohování do RPi5
category: Počítače
tags: [linux, zalohovani, RPi, kyberbezpečnost]
last_update: 2025-07-19
---

# 🚀 Kompletní návod: Šifrovaný intranetový cloud pro zálohování ze dvou Windows notebooků na RPi5 s NVMe diskem

# 1️⃣ Příprava RPi: aktualizace a složky
sudo apt update && sudo apt upgrade -y
sudo mkdir -p /mnt/cloud-notebook1-container /mnt/cloud-notebook2-container

# (Pokud NVMe ještě není připojený)
lsblk  # zkontroluj zařízení
sudo mkfs.ext4 /dev/nvme0n1p1  # POZOR: smaže data!
sudo mount /dev/nvme0n1p1 /mnt

# 2️⃣ Vytvoření prázdných VeraCrypt kontejnerů (50GB)
sudo fallocate -l 50G /mnt/cloud-notebook1-container/backup1.vc
sudo fallocate -l 50G /mnt/cloud-notebook2-container/backup2.vc

# 3️⃣ Na Windows:
# - vytvoř kontejnery přes VeraCrypt GUI (https://www.veracrypt.fr/en/Downloads.html)
# - nastav silné heslo, souborový systém NTFS/ext4
# - přenes kontejnerové soubory (.vc) zpět na RPi do příslušných složek

# 4️⃣ Instalace balíčků na RPi
sudo apt install veracrypt openssh-server samba -y
sudo systemctl enable --now ssh

# 5️⃣ Připojení VeraCrypt kontejnerů na RPi (přidej své heslo)
sudo veracrypt --mount /mnt/cloud-notebook1-container/backup1.vc /mnt/cloud-notebook1 --password="TvojeSilneHeslo" --non-interactive
sudo veracrypt --mount /mnt/cloud-notebook2-container/backup2.vc /mnt/cloud-notebook2 --password="TvojeSilneHeslo" --non-interactive

# 6️⃣ Samba sdílení (volitelné)
# Uprav /etc/samba/smb.conf přidáním:
# [notebook1]
#   path = /mnt/cloud-notebook1
#   valid users = liko
#   read only = no
#
# [notebook2]
#   path = /mnt/cloud-notebook2
#   valid users = liko
#   read only = no

sudo smbpasswd -a liko
sudo systemctl restart smbd

# 7️⃣ Zálohování z Windows
# - Připoj Samba sdílení v Průzkumníku: \\IP_RPi\notebook1 a \\IP_RPi\notebook2
# - Nebo rsync přes WSL / DeltaCopy:
#   rsync -avz /mnt/c/Users/uzivatel/Documents/ liko@IP_RPi:/mnt/cloud-notebook1/

# 8️⃣ Automatický skript na RPi pro zálohy:
cat << 'EOF' > ~/backup-cloud.sh
#!/bin/bash
veracrypt --mount /mnt/cloud-notebook1-container/backup1.vc /mnt/cloud-notebook1 --password="TvojeSilneHeslo" --non-interactive
veracrypt --mount /mnt/cloud-notebook2-container/backup2.vc /mnt/cloud-notebook2 --password="TvojeSilneHeslo" --non-interactive

rsync -av --delete /home/liko/notebook1_data/ /mnt/cloud-notebook1/
rsync -av --delete /home/liko/notebook2_data/ /mnt/cloud-notebook2/

veracrypt -d /mnt/cloud-notebook1
veracrypt -d /mnt/cloud-notebook2
EOF

chmod +x ~/backup-cloud.sh

# 9️⃣ Automatické připojení VeraCrypt kontejnerů při startu RPi

# Vytvoř systemd službu:
cat << 'EOF' | sudo tee /etc/systemd/system/veracrypt-mount.service
[Unit]
Description=Mount VeraCrypt containers at boot
After=network-online.target
Wants=network-online.target

[Service]
Type=oneshot
ExecStart=/usr/bin/veracrypt --mount /mnt/cloud-notebook1-container/backup1.vc /mnt/cloud-notebook1 --password="TvojeSilneHeslo" --non-interactive
ExecStart=/usr/bin/veracrypt --mount /mnt/cloud-notebook2-container/backup2.vc /mnt/cloud-notebook2 --password="TvojeSilneHeslo" --non-interactive
RemainAfterExit=yes

[Install]
WantedBy=multi-user.target
EOF

# Aktivuj službu:
sudo systemctl daemon-reload
sudo systemctl enable veracrypt-mount.service
sudo systemctl start veracrypt-mount.service

# 10️⃣ PowerShell skript pro Windows zálohy na RPi (pomocí rsync přes WSL)

# Ulož jako backup.ps1 na Windows (upravit IP a cesty):

$source1 = "C:\Users\uzivatel\Documents\"
$source2 = "C:\Users\uzivatel\Pictures\"
$dest1 = "liko@IP_RPi:/mnt/cloud-notebook1/"
$dest2 = "liko@IP_RPi:/mnt/cloud-notebook2/"

# Nastav cestu k WSL rsync
$rsync = "C:\Windows\System32\wsl.exe"

Write-Host "Spouštím zálohu Documents..."
& $rsync rsync -avz --delete "$source1" "$dest1"

Write-Host "Spouštím zálohu Pictures..."
& $rsync rsync -avz --delete "$source2" "$dest2"

Write-Host "Zálohování dokončeno."

# ------------------------------------
# 🔗 Užitočné zdroje:
# - VeraCrypt: https://www.veracrypt.fr/en/Home.html
# - Rsync for Windows (WSL): https://learn.microsoft.com/en-us/windows/wsl/
# - Samba: https://www.samba.org/samba/docs/current/man-html/smb.conf.5.html
# - RPi NVMe disk setup: https://www.raspberrypi.com/documentation/computers/storage.html


# 🚀 Rozšířený návod: Automatizace záloh na Windows + šifrování dat při zálohování na RPi5

# 1️⃣ Automatické spouštění PowerShell zálohy pomocí Plánovače úloh (Task Scheduler) ve Windows:

# - Otevři Task Scheduler (Plánovač úloh)
# - Klikni na "Create Basic Task..."
# - Dej název např. "Záloha na RPi"
# - Nastav spouštění (denně, při startu apod.)
# - Akce: "Start a program"
# - Program/script: powershell.exe
# - Přidej argumenty: -File "C:\cesta\k\backup.ps1"
# - Dokonči průvodce

# Pro kontrolu, že běží, můžeš přidat do backup.ps1 logování, např.:

Add-Content -Path "C:\Users\uzivatel\backup.log" -Value "$(Get-Date): Záloha spuštěna"

# 2️⃣ Šifrování dat na cestě přes SSH tunel pro rsync:

# V PowerShell skriptu nahraď rsync příkaz tímto:

$rsyncCmd = "rsync -avz -e `"ssh -p 22`" --delete `"$source1`" `"$dest1`""
Invoke-Expression $rsyncCmd

# nebo pokud používáš wsl.exe:

$rsyncCmd1 = "rsync -avz -e 'ssh -p 22' --delete '$source1' '$dest1'"
$rsyncCmd2 = "rsync -avz -e 'ssh -p 22' --delete '$source2' '$dest2'"

& wsl.exe $rsyncCmd1
& wsl.exe $rsyncCmd2

# 3️⃣ Doporučení pro zabezpečení:

# - Používej SSH klíče místo hesel pro přihlášení na RPi (generování: ssh-keygen)
# - Zakázat přihlášení heslem na RPi (v /etc/ssh/sshd_config: PasswordAuthentication no)
# - Používej silná hesla pro VeraCrypt kontejnery
# - Omez přístup ke sdíleným složkám Samba jen na důvěryhodné IP adresy
# - Pravidelně aktualizuj RPi a Windows
# - Zvaž zálohu kontejnerů na další offline médium

# ------------------------------------
# 🔗 Užitočné zdroje:
# - Windows Task Scheduler: https://learn.microsoft.com/en-us/windows/win32/taskschd/task-scheduler-start-page
# - SSH keygen a konfigurace: https://linuxize.com/post/how-to-set-up-ssh-keys-on-ubuntu-20-04/
# - Rsync přes SSH: https://linuxize.com/post/how-to-use-rsync-for-local-and-remote-data-transfer-and-synchronization/
# - VeraCrypt bezpečnostní doporučení: https://www.veracrypt.fr/en/Security%20Guide.html

# 🚀 Kompletní automatizace záloh Windows -> RPi5 s VeraCrypt kontejnery + SSH šifrování + plánovač úloh

# 1️⃣ Generování SSH klíčů na Windows (PowerShell nebo Git Bash):
ssh-keygen -t ed25519 -C "tvuj_email@domena.cz"
# Nech heslo prázdné nebo nastav silné (doporučeno)
# Výchozí umístění: C:\Users\uzivatel\.ssh\id_ed25519 a id_ed25519.pub

# 2️⃣ Nahrání veřejného klíče na RPi (pro uživatele 'liko'):
scp ~/.ssh/id_ed25519.pub liko@IP_RPi:~/
ssh liko@IP_RPi

# Na RPi:
mkdir -p ~/.ssh
cat ~/id_ed25519.pub >> ~/.ssh/authorized_keys
chmod 700 ~/.ssh
chmod 600 ~/.ssh/authorized_keys
rm ~/id_ed25519.pub

# 3️⃣ Zakázání přihlášení heslem na RPi:
sudo nano /etc/ssh/sshd_config
# Najdi a uprav nebo přidej:
PasswordAuthentication no
# Restart SSH služby:
sudo systemctl restart ssh

# 4️⃣ PowerShell skript zálohy s rsync přes SSH (ulož např. jako backup.ps1):

$source1 = "C:\Users\uzivatel\Documents\"
$source2 = "C:\Users\uzivatel\Pictures\"
$dest1 = "liko@IP_RPi:/mnt/cloud-notebook1/"
$dest2 = "liko@IP_RPi:/mnt/cloud-notebook2/"
$rsync = "C:\Windows\System32\wsl.exe"

Write-Host "Spouštím zálohu Documents přes SSH..."
& $rsync rsync -avz -e "ssh -i /mnt/c/Users/uzivatel/.ssh/id_ed25519 -p 22" --delete "$source1" "$dest1"

Write-Host "Spouštím zálohu Pictures přes SSH..."
& $rsync rsync -avz -e "ssh -i /mnt/c/Users/uzivatel/.ssh/id_ed25519 -p 22" --delete "$source2" "$dest2"

Write-Host "Zálohování dokončeno."

# 5️⃣ Naplánování automatické zálohy pomocí Plánovače úloh Windows:

# - Otevři Plánovač úloh (Task Scheduler)
# - Klikni na "Create Basic Task..."
# - Název: "Záloha na RPi přes SSH"
# - Spouštění: např. denně v 3:00 ráno
# - Akce: Start a program
# - Program/script: powershell.exe
# - Přidej argumenty: -File "C:\cesta\k\backup.ps1"
# - Dokonči a zkontroluj, že úloha funguje

# 6️⃣ Na RPi: automatické připojení VeraCrypt kontejnerů při startu

sudo tee /etc/systemd/system/veracrypt-mount.service > /dev/null << 'EOF'
[Unit]
Description=Mount VeraCrypt containers at boot
After=network-online.target
Wants=network-online.target

[Service]
Type=oneshot
ExecStart=/usr/bin/veracrypt --mount /mnt/cloud-notebook1-container/backup1.vc /mnt/cloud-notebook1 --password="TvojeSilneHeslo" --non-interactive
ExecStart=/usr/bin/veracrypt --mount /mnt/cloud-notebook2-container/backup2.vc /mnt/cloud-notebook2 --password="TvojeSilneHeslo" --non-interactive
RemainAfterExit=yes

[Install]
WantedBy=multi-user.target
EOF

sudo systemctl daemon-reload
sudo systemctl enable veracrypt-mount.service
sudo systemctl start veracrypt-mount.service

# 7️⃣ Doporučení zabezpečení:

# - Používej SSH klíče, ne hesla
# - Zakázat hesla na SSH na RPi
# - Silná hesla pro VeraCrypt kontejnery
# - Omez přístup Samba na interní IP adresy
# - Pravidelně aktualizuj systém a software
# - Zálohuj kontejnerové soubory i na offline médium

# ------------------------------------
# 🔗 Užitočné zdroje:
# - SSH klíče na Windows: https://docs.microsoft.com/en-us/windows-server/administration/openssh/openssh_keymanagement
# - Rsync přes SSH v PowerShell: https://stackoverflow.com/questions/30437510/how-to-run-rsync-on-windows
# - VeraCrypt: https://www.veracrypt.fr/en/Home.html
# - Systemd služba: https://www.freedesktop.org/software/systemd/man/systemd.service.html
# - Windows Task Scheduler: https://learn.microsoft.com/en-us/windows/win32/taskschd/task-scheduler-start-page

# 🔑 Detailní návod: Nastavení SSH klíčů Windows -> RPi, PowerShell záloha s logy a zabezpečený Samba přístup

# 1️⃣ Generování SSH klíčů na Windows

# Otevři PowerShell nebo Git Bash a spusť:
ssh-keygen -t ed25519 -C "tvuj_email@domena.cz"

# - Přijmi výchozí umístění (C:\Users\uzivatel\.ssh\id_ed25519)
# - Nastav silné heslo nebo ponech prázdné (doporučeno heslo)
# - Po dokončení bys měl mít dva soubory:
#    - id_ed25519 (soukromý klíč)
#    - id_ed25519.pub (veřejný klíč)

# 2️⃣ Přenos veřejného klíče na RPi

scp C:\Users\uzivatel\.ssh\id_ed25519.pub liko@IP_RPi:~

# Přihlas se na RPi:
ssh liko@IP_RPi

# Na RPi spusť:
mkdir -p ~/.ssh
cat ~/id_ed25519.pub >> ~/.ssh/authorized_keys
chmod 700 ~/.ssh
chmod 600 ~/.ssh/authorized_keys
rm ~/id_ed25519.pub

# 3️⃣ Ověření, že SSH přihlášení funguje bez hesla:

ssh -i ~/.ssh/id_ed25519 liko@IP_RPi

# Pokud se přihlásíš bez zadání hesla, je vše OK.

# 4️⃣ Zakázání přihlášení heslem na RPi pro vyšší bezpečnost:

sudo nano /etc/ssh/sshd_config

# Najdi řádek:
# PasswordAuthentication yes
# a změň na:
PasswordAuthentication no

# Ulož a restartuj SSH službu:
sudo systemctl restart ssh

# 5️⃣ PowerShell skript zálohy s logováním a ošetřením chyb (backup.ps1):

$logFile = "C:\Users\uzivatel\backup.log"
function LogWrite($msg) {
    $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    Add-Content -Path $logFile -Value "$timestamp : $msg"
}

try {
    LogWrite "=== Záloha spuštěna ==="

    $source1 = "C:\Users\uzivatel\Documents\"
    $source2 = "C:\Users\uzivatel\Pictures\"
    $dest1 = "liko@IP_RPi:/mnt/cloud-notebook1/"
    $dest2 = "liko@IP_RPi:/mnt/cloud-notebook2/"
    $rsync = "C:\Windows\System32\wsl.exe"

    LogWrite "Záloha Documents spuštěna..."
    & $rsync rsync -avz -e "ssh -i /mnt/c/Users/uzivatel/.ssh/id_ed25519 -p 22" --delete "$source1" "$dest1"
    if ($LASTEXITCODE -ne 0) {
        LogWrite "Chyba při záloze Documents!"
        throw "Rsync selhal"
    }

    LogWrite "Záloha Pictures spuštěna..."
    & $rsync rsync -avz -e "ssh -i /mnt/c/Users/uzivatel/.ssh/id_ed25519 -p 22" --delete "$source2" "$dest2"
    if ($LASTEXITCODE -ne 0) {
        LogWrite "Chyba při záloze Pictures!"
        throw "Rsync selhal"
    }

    LogWrite "=== Záloha dokončena úspěšně ==="
}
catch {
    LogWrite "Výjimka: $_"
}

# 6️⃣ Nastavení zabezpečeného Samba přístupu na RPi

sudo nano /etc/samba/smb.conf

# Přidej na konec:

[notebook1]
   path = /mnt/cloud-notebook1
   valid users = liko
   read only = no
   hosts allow = 10.20.1.0/24 192.168.1.0/24 127.0.0.1
   # povolit přístup jen z lokální sítě, uprav podle své sítě

[notebook2]
   path = /mnt/cloud-notebook2
   valid users = liko
   read only = no
   hosts allow = 10.20.1.0/24 192.168.1.0/24 127.0.0.1

# Restartuj Samba službu:
sudo systemctl restart smbd

# 7️⃣ Další tipy zabezpečení Samba:

# - Použij silné heslo uživatele 'liko':
sudo smbpasswd liko
# - Pravidelně kontroluj /var/log/samba/log.smbd pro podezřelé aktivity
# - Omez přístup pomocí firewallu (ufw nebo iptables)
#   např. sudo ufw allow from 10.20.1.0/24 to any port 445 proto tcp

# ------------------------------------
# 🔗 Užitočné zdroje:
# - SSH klíče: https://linuxize.com/post/how-to-set-up-ssh-keys-on-ubuntu/
# - PowerShell logování: https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/add-content
# - Samba hosts allow: https://www.samba.org/samba/docs/current/man-html/smb.conf.5.html
# - Rsync pro Windows: https://stackoverflow.com/questions/30437510/how-to-run-rsync-on-windows

# 1️⃣ Hotový Task Scheduler export (XML)

# Tento soubor můžeš importovat ve Windows Plánovači úloh (Task Scheduler) přes:
# Action → Import Task...

<?xml version="1.0" encoding="UTF-16"?>
<Task version="1.4" xmlns="http://schemas.microsoft.com/windows/2004/02/mit/task">
  <RegistrationInfo>
    <Date>2025-07-19T08:00:00</Date>
    <Author>uzivatel</Author>
    <Description>Záloha na RPi přes SSH s PowerShellem</Description>
  </RegistrationInfo>
  <Triggers>
    <CalendarTrigger>
      <StartBoundary>2025-07-20T03:00:00</StartBoundary>
      <ScheduleByDay>
        <DaysInterval>1</DaysInterval>
      </ScheduleByDay>
      <Enabled>true</Enabled>
    </CalendarTrigger>
  </Triggers>
  <Principals>
    <Principal id="Author">
      <UserId>uzivatel</UserId>
      <RunLevel>LeastPrivilege</RunLevel>
    </Principal>
  </Principals>
  <Settings>
    <MultipleInstancesPolicy>IgnoreNew</MultipleInstancesPolicy>
    <DisallowStartIfOnBatteries>true</DisallowStartIfOnBatteries>
    <StopIfGoingOnBatteries>true</StopIfGoingOnBatteries>
    <AllowHardTerminate>true</AllowHardTerminate>
    <StartWhenAvailable>true</StartWhenAvailable>
    <RunOnlyIfNetworkAvailable>true</RunOnlyIfNetworkAvailable>
    <IdleSettings>
      <StopOnIdleEnd>true</StopOnIdleEnd>
      <RestartOnIdle>false</RestartOnIdle>
    </IdleSettings>
    <AllowStartOnDemand>true</AllowStartOnDemand>
    <Enabled>true</Enabled>
    <Hidden>false</Hidden>
    <RunOnlyIfIdle>false</RunOnlyIfIdle>
    <WakeToRun>false</WakeToRun>
    <ExecutionTimeLimit>PT1H</ExecutionTimeLimit>
    <Priority>7</Priority>
  </Settings>
  <Actions Context="Author">
    <Exec>
      <Command>powershell.exe</Command>
      <Arguments>-File "C:\cesta\k\backup.ps1"</Arguments>
    </Exec>
  </Actions>
</Task>

# ------------------------------------

# 2️⃣ RPi automatizovaná instalace a konfigurace Samba + firewall (bash script)

sudo tee ~/setup_samba_firewall.sh > /dev/null << 'EOF'
#!/bin/bash
set -e

echo "Aktualizuji systém..."
sudo apt update && sudo apt upgrade -y

echo "Instaluji Samba..."
sudo apt install samba -y

echo "Vytvářím sdílení pro cloud-notebook1 a cloud-notebook2..."

sudo mkdir -p /mnt/cloud-notebook1 /mnt/cloud-notebook2
sudo chown liko:liko /mnt/cloud-notebook1 /mnt/cloud-notebook2

sudo bash -c 'cat >> /etc/samba/smb.conf' << EOL

[notebook1]
   path = /mnt/cloud-notebook1
   valid users = liko
   read only = no
   hosts allow = 10.20.1.0/24 192.168.1.0/24 127.0.0.1

[notebook2]
   path = /mnt/cloud-notebook2
   valid users = liko
   read only = no
   hosts allow = 10.20.1.0/24 192.168.1.0/24 127.0.0.1
EOL

echo "Nastavuji Samba uživatele (nastav heslo pro 'liko')..."
sudo smbpasswd -a liko
sudo smbpasswd -e liko

echo "Restartuji Samba službu..."
sudo systemctl restart smbd

echo "Instaluji a konfiguruj firewall UFW..."

sudo apt install ufw -y
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw allow ssh
sudo ufw allow from 10.20.1.0/24 to any port 445 proto tcp
sudo ufw allow from 192.168.1.0/24 to any port 445 proto tcp
sudo ufw enable

echo "Samba a firewall nastaveny!"
EOF

chmod +x ~/setup_samba_firewall.sh
echo "Spusť příkaz: ./setup_samba_firewall.sh jako uživatel 'liko' s sudo právy."

# ------------------------------------

# 3️⃣ PowerShell skript s e-mailovou notifikací po záloze

$logFile = "C:\Users\uzivatel\backup.log"
$smtpServer = "smtp.tvoje-domena.cz"
$smtpPort = 587
$smtpUser = "uzivatel@tvoje-domena.cz"
$smtpPass = "TvojeHeslo"
$toEmail = "uzivatel@tvoje-domena.cz"
$fromEmail = "backup@tvoje-domena.cz"
$subject = "Záloha na RPi dokončena"
$bodySuccess = "Záloha byla dokončena úspěšně.`nViz přiložený log."
$bodyFail = "Záloha selhala! Viz log."

function LogWrite($msg) {
    $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    Add-Content -Path $logFile -Value "$timestamp : $msg"
}

function Send-Email($subject, $body) {
    $message = New-Object System.Net.Mail.MailMessage
    $message.From = $fromEmail
    $message.To.Add($toEmail)
    $message.Subject = $subject
    $message.Body = $body
    $smtp = New-Object Net.Mail.SmtpClient($smtpServer, $smtpPort)
    $smtp.EnableSsl = $true
    $smtp.Credentials = New-Object System.Net.NetworkCredential($smtpUser, $smtpPass)
    $smtp.Send($message)
}

try {
    LogWrite "=== Záloha spuštěna ==="

    # zde zavoláš rsync jak dříve
    # např. & wsl.exe rsync -avz -e "ssh -i /mnt/c/Users/uzivatel/.ssh/id_ed25519" --delete $source $dest

    LogWrite "=== Záloha dokončena úspěšně ==="
    Send-Email $subject $bodySuccess
}
catch {
    LogWrite "Výjimka: $_"
    Send-Email $subject $bodyFail
}


# 🔥 Další pokročilé automatizace a zabezpečení intranetového cloudu na RPi + Windows zálohy

# 1️⃣ Automatické připojení VeraCrypt kontejnerů při startu RPi

# Nainstaluj VeraCrypt (pokud nemáš):
sudo apt install veracrypt -y

# Vytvoř shell skript např. ~/mount-veracrypt.sh:

cat > ~/mount-veracrypt.sh << 'EOF'
#!/bin/bash
# Mount VeraCrypt container automaticky při startu

# Cesta k VeraCrypt souborům
CONTAINER1="/mnt/veracrypt/cloud-notebook1.hc"
CONTAINER2="/mnt/veracrypt/cloud-notebook2.hc"

# Mount pointy
MOUNT1="/mnt/cloud-notebook1"
MOUNT2="/mnt/cloud-notebook2"

# Hesla (doporučeno lepší zabezpečení, např. keyfile nebo prompt)
PASS1="TvojeSilneHeslo1"
PASS2="TvojeSilneHeslo2"

veracrypt --text --non-interactive --password="$PASS1" --mount "$CONTAINER1" "$MOUNT1"
veracrypt --text --non-interactive --password="$PASS2" --mount "$CONTAINER2" "$MOUNT2"
EOF

chmod +x ~/mount-veracrypt.sh

# Přidej spouštění do crontabu pro root, aby se spustilo při startu:

sudo crontab -e

# Přidej řádek:
@reboot /home/liko/mount-veracrypt.sh

# 2️⃣ Windows PowerShell skript pro zálohy na VeraCrypt připojené sdílení

$logFile = "C:\Users\uzivatel\backup.log"
$source1 = "C:\Users\uzivatel\Documents\"
$source2 = "C:\Users\uzivatel\Pictures\"
$dest1 = "\\RPi5\notebook1"
$dest2 = "\\RPi5\notebook2"

function LogWrite($msg) {
    $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    Add-Content -Path $logFile -Value "$timestamp : $msg"
}

try {
    LogWrite "=== Záloha spuštěna ==="

    LogWrite "Záloha Documents spuštěna..."
    robocopy $source1 $dest1 /MIR /Z /R:3 /W:5 /LOG+:$logFile
    if ($LASTEXITCODE -ge 8) { throw "Robocopy chyba" }

    LogWrite "Záloha Pictures spuštěna..."
    robocopy $source2 $dest2 /MIR /Z /R:3 /W:5 /LOG+:$logFile
    if ($LASTEXITCODE -ge 8) { throw "Robocopy chyba" }

    LogWrite "=== Záloha dokončena úspěšně ==="
}
catch {
    LogWrite "Výjimka: $_"
}

# 3️⃣ Šifrování dat na cestě: použití SSH tunelu a AES šifrovaných protokolů

# Doporučuji rsync přes SSH (už máme), případně VPN tunel (WireGuard):

# Základní nastavení WireGuard mezi Windows a RPi:

# Na RPi:
sudo apt install wireguard -y
wg genkey | tee privatekey | wg pubkey > publickey

# Na Windows: stáhni WireGuard client, nastav konfiguraci s privátní a veřejnou klíčem, adresou apod.

# Pak přesměruješ zálohy přes WireGuard VPN – veškerá komunikace je bezpečně šifrovaná.

# 4️⃣ Automatické spouštění PowerShell skriptu přes Task Scheduler

# Použij XML export ze dřívějška nebo vytvoř úlohu:

# powershell.exe -File "C:\cesta\k\backup.ps1"

# Naplánuj denní či hodinové spuštění, podle potřeby.

# ------------------------------------

# 🧰 Tipy pro další zabezpečení:

# - Pravidelně zálohuj SSH klíče a VeraCrypt kontejnery offline
# - Používej silná hesla + keyfiles u VeraCrypt
# - Omez přístup přes firewall, whitelist IP adres
# - Loguj a monitoruj neúspěšné pokusy o přístup
# - Udržuj systém aktuální (RPi i Windows)
# - Zvaž automatizované upozornění (e-mail, Telegram bot)

# ------------------------------------

# 🔗 Zdrojové reference:

# - VeraCrypt command line: https://www.veracrypt.fr/en/Command%20Line%20Usage.html
# - WireGuard quickstart: https://www.wireguard.com/quickstart/
# - Robocopy dokumentace: https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/robocopy
# - PowerShell logging best practices: https://devblogs.microsoft.com/powershell/powershell-tracing-and-logging/



