### 🛠️ Instalace potřebných balíčků
    sudo apt update
    sudo apt install mutt gnupg gpg-agent msmtp ca-certificates mbsync python3-requests python3-oauthlib python3-keyring

### 📁 Vytvoření potřebných adresářů a souborů
    mkdir -p ~/.mutt/cache ~/.mail/{INBOX,Sent,Drafts} ~/.mutt-oauth2
    touch ~/.mutt/muttrc ~/.mailpw.gpg ~/.mutt-oauth2/token.gpg
    chmod 600 ~/.mailpw.gpg ~/.mutt-oauth2/token.gpg

### 🧩 Konfigurace Mutt (~/.mutt/muttrc)
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
    set imap_authenticators = "oauthbearer"
    set smtp_authenticators = "oauthbearer"
    set imap_oauth_refresh_command = "python3 ~/.mutt-oauth2/mutt_oauth2.py ~/.mutt-oauth2/token.gpg"
    set smtp_oauth_refresh_command = "python3 ~/.mutt-oauth2/mutt_oauth2.py ~/.mutt-oauth2/token.gpg"

### 🎨 Barvy pro index view
    color index brightcyan default ~N  # Nové zprávy
    color index brightyellow default ~F  # Flagged zprávy
    color index green default ~T  # Odeslané zprávy
    color index brightred default ~D  # Smazané zprávy
    mono index bold ~N  # Zvýraznění nových zpráv
    mono index bold ~F  # Zvýraznění flagovaných zpráv
    mono index bold ~T  # Zvýraznění odeslaných zpráv
    mono index bold ~D  # Zvýraznění smazaných zpráv

    color index brightgreen default ~f"odesílatel@example.com" # Tato konfigurace zvýrazní zprávy od odesílatele odesílatel@example.com zeleně.

### 🔐 GPG šifrování a podpis
    set crypt_use_gpgme = yes
    set crypt_autosign = yes
    set crypt_autoencrypt = yes
    set crypt_replyencrypt = yes
    set crypt_replysign = yes
    set crypt_replysignencrypted = yes

### 🔄 Volitelné: spustit gpg-agent při startu Mutt
    set my_msmtp_pass=`gpg --quiet --no-tty --for-your-eyes-only --decrypt ~/.mailpw.gpg`

### 📧 Konfigurace msmtp (~/.msmtprc)
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

### 🔐 Uložení hesla SMTP
    echo "TvojeSMTP_Heslo" | gpg --default-recipient-self --encrypt > ~/.mailpw.gpg
    chmod 600 ~/.mailpw.gpg

### 🧪 Konfigurace gpg-agent (např. v ~/.bashrc)
    eval $(gpg-agent --daemon --enable-ssh-support --write-env-file ~/.gpg-agent-info)
    export GPG_AGENT_INFO
    export SSH_AUTH_SOCK=$(grep -R SSH_AUTH_SOCK ~/.gpg-agent-info | cut -d'=' -f2-)
    export GPG_TTY=$(tty)

### 📥 Konfigurace mbsync (~/.mbsyncrc)
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

### 🔄 Spuštění synchronizace
    mbsync sync

### 📬 Spuštění Mutt
    mutt

### 🕒 Automatická synchronizace pomocí cron
    crontab -e
    # Přidejte následující řádek pro synchronizaci každých 15 minut
    */15 * * * * mbsync sync

### 🔑 Generování a správa OAuth2 tokenu
    wget https://gitlab.com/muttmua/mutt/-/raw/master/contrib/mutt_oauth2.py -O ~/.mutt-oauth2/mutt_oauth2.py
    chmod +x ~/.mutt-oauth2/mutt_oauth2.py
    python3 ~/.mutt-oauth2/mutt_oauth2.py ~/.mutt-oauth2/token.gpg --authorize

    # Pro obnovení tokenu
    python3 ~/.mutt-oauth2/mutt_oauth2.py ~/.mutt-oauth2/token.gpg --refresh

### 🧠 Tipy a triky
- **Klávesové zkratky v Mutt**:
  - `m` = napsat zprávu
  - `c` = změna složky
  - `g` = načíst novou poštu po mbsync
  - `q` = ukončení

- **Bezpečnostní tip**: Používej `passwordeval` s GPG pro šifrované heslo místo ukládání v plaintextu. [wiki.archlinux.org](https://wiki.archlinux.org/title/MSMTP)

- **Synchronizace s IMAP**: `mbsync` efektivně synchronizuje složky mezi serverem a lokálním Maildir. [isync.sourceforge.io](https://isync.sourceforge.io/mbsync.html)

- **Automatické spuštění gpg-agent**: Použití `eval $(gpg-agent --daemon ...)` v `~/.bashrc` zajistí, že gpg-agent bude spuštěn při každém přihlášení. [cryptomonkeys.com](https://cryptomonkeys.com/2015/09/mutt-and-msmtp-on-osx/)

- **OAuth2 s Gmail**: Pro Gmail použij `oauthbearer` autentizaci. [wiki.archlinux.org](https://wiki.archlinux.org/title/MSMTP)

- **OAuth2 s Microsoft
::contentReference[oaicite:5]{index=5}
 
