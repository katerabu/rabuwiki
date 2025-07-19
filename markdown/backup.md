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
