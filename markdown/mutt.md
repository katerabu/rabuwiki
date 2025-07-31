# 🛠️ Instalace potřebných balíčků
sudo apt update
sudo apt install mutt gnupg gpg-agent msmtp ca-certificates mbsync

# 📁 Vytvoření adresářové struktury a souborů
mkdir -p ~/.mutt/cache ~/.mail/{INBOX,Sent,Drafts}
touch ~/.mutt/muttrc ~/.mailpw.gpg
chmod 600 ~/.mailpw.gpg

# 🧩 Konfigurace Mutt (~/.mutt/muttrc)
set realname = "Tvůj Nick"
set from = "[email protected]"
set use_from = yes
set envelope_from = yes
set sendmail="/usr/bin/msmtp"
set editor="nano"
set charset="utf-8"
set folder = "~/.mail"
set spoolfile = "+INBOX"
set record = "+Sent"
set postponed = "+Drafts"

# 🎨 Barvy index view
color index brightcyan default ~N
color index brightyellow default ~F
color index green default ~T
color index brightred default ~D
color quoted cyan default
color signature brightmagenta default
color status brightwhite blue
color tree brightyellow default
color error brightred default
color search brightwhite magenta

# 🔐 GPG šifrování a podpis
set crypt_use_gpgme = yes
set crypt_autosign = yes
set crypt_autoencrypt = yes
set crypt_replyencrypt = yes
set crypt_replysign = yes
set crypt_replysignencrypted = yes

# 🔄 Volitelné: spustit gpg-agent při startu Mutt
set my_msmtp_pass=`gpg --quiet --no-tty --for-your-eyes-only --decrypt ~/.mailpw.gpg`

# 📧 Konfigurace msmtp (~/.msmtprc)
defaults
auth on
tls on
tls_starttls on
tls_trust_file /etc/ssl/certs/ca-certificates.crt

account default
host smtp.example.com
port 587
from [email protected]
user [email protected]
passwordeval "gpg --quiet --no-tty --for-your-eyes-only --decrypt ~/.mailpw.gpg"

# 🔐 Uložení hesla SMTP
echo "TvojeSMTP_Heslo" | gpg --default-recipient-self --encrypt > ~/.mailpw.gpg
chmod 600 ~/.mailpw.gpg

# 🧪 Konfigurace gpg-agent (např. v ~/.bashrc)
eval $(gpg-agent --daemon --enable-ssh-support --write-env-file ~/.gpg-agent-info)
export GPG_AGENT_INFO
export SSH_AUTH_SOCK=$(grep -R SSH_AUTH_SOCK ~/.gpg-agent-info | cut -d'=' -f2-)
export GPG_TTY=$(tty)

## 🧪 Konfigurace gpg-agent (např. v ~/.bashrc)
eval $(gpg-agent --daemon --enable-ssh-support --write-env-file ~/.gpg-agent-info)
export GPG_AGENT_INFO
export SSH_AUTH_SOCK=$(grep -R SSH_AUTH_SOCK ~/.gpg-agent-info | cut -d'=' -f2-)
export GPG_TTY=$(tty)

# 📥 Konfigurace mbsync (~/.mbsyncrc)
IMAPAccount account
Host imap.example.com
User [email protected]
PassCmd "gpg --quiet --decrypt ~/.mailpw.gpg"
SSLType IMAPS
CertificateFile /etc/ssl/certs/ca-certificates.crt

IMAPStore store account
MaildirStore local ~/.mail/
Channel sync
Master :account:
Slave local
Patterns *
Create Slave
Sync Pull

# 🔄 Spuštění synchronizace
mbsync sync

# 📬 Spuštění Mutt
mutt

# 🧠 Tipy a triky
Klávesové zkratky v Mutt:
m = napsat zprávu
c = změna složky
g = načíst novou poštu po mbsync
q = ukončení
Bezpečnostní tip: Používej passwordeval s GPG pro šifrované heslo místo ukládání v plaintextu.
Synchronizace s IMAP: mbsync efektivně synchronizuje složky mezi serverem a lokálním Maildir.
Automatické spuštění gpg-agent: Použití eval $(gpg-agent --daemon ...) v ~/.bashrc zajistí, že gpg-agent bude spuštěn při každém přihlášení.
