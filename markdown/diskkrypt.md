## 🔐 Disková kryptografie (Disk Encryption)

### 🧾 Co je disková kryptografie?

Disková kryptografie slouží k **ochraně uložených dat** před neoprávněným přístupem – i v případě fyzické krádeže zařízení. Šifrování může být aplikováno na:

- **celý disk** (Full Disk Encryption – FDE)
- **oddíl/discový svazek**
- **soubory/složky**

> „Encryption is the last line of defense – if your system is compromised or stolen, your data remains unreadable.“  
> – Schneier, B. (2015). *Data and Goliath*

---

### 🧱 Typy šifrování

```
    +---------------------------+
    |   Typy šifrování disku   |
    +---------------------------+
    | 🔒 Full Disk Encryption   |
    | 🗂️ File/Folder Encryption |
    | 📁 Container (e.g. VeraCrypt) |
    +---------------------------+
```

| Typ                | Vlastnosti | Vhodné použití |
|--------------------|------------|----------------|
| **FDE (např. BitLocker)** | Šifruje celý disk včetně OS | Notebooky, firemní stanice |
| **File-based (např. EFS)**| Šifrování na úrovni souborů | Dokumenty, sdílené disky |
| **Kontejnery (VeraCrypt)**| Virtuální disk se šifrovaným obsahem | Přenosná média, citlivé složky |
| **Hybridní přístup**       | Kombinace více typů | Vysoká bezpečnost |

---

### 🔑 Algoritmy a standardy

- **AES-256** – nejčastější standard (symetrický blokový algoritmus)
- **XTS-AES** – bezpečnější mód pro šifrování blokových zařízení
- **LUKS** – standardní formát pro šifrování disků na Linuxu (dm-crypt)
- **BitLocker** – proprietární technologie od Microsoftu (Windows Pro+)
- **FileVault 2** – šifrování disku od Apple (macOS)

📌 Doporučeno: **AES-256 + XTS** s dlouhým heslem nebo klíčem chráněným TPM/HSM

---

### 💡 Doporučené nástroje

| Nástroj        | Platforma | Poznámka |
|----------------|-----------|----------|
| **BitLocker**  | Windows   | Integrace s OS, TPM, bezplatný |
| **FileVault 2**| macOS     | Výchozí volba na Macu |
| **LUKS/dm-crypt** | Linux   | Flexibilní, podporuje klíče i hesla |
| **VeraCrypt**  | Cross-platform | Silné šifrování, skryté kontejnery |
| **Zed!**       | Windows   | Šifrování souborů/folderů (alternativa k ZIP + heslo) |

---

### 🧯 Hrozby a bezpečnostní doporučení

| Riziko                                | Ochrana |
|---------------------------------------|---------|
| ❌ Špatně zvolené heslo               | Použij silnou passphrase (např. 6+ náhodných slov) |
| ❌ Uspání místo vypnutí zařízení      | Útok přes RAM (Cold Boot Attack) |
| ❌ Nechráněný boot (bez hesla v BIOSu)| Nastavit BIOS heslo, zakázat boot z USB |
| ❌ Nešifrovaný swap/hibernační oddíl  | Zahrnout do šifrování |
| ❌ Přístup v běhu systému (Evil Maid) | Fyzická ochrana, podpis bootloaderu, Secure Boot |

📌 Vždy vypínej zařízení, neuspávej. Šifrování nechrání běžící OS před útoky.

---

### 🔐 ASCII diagram – jak funguje FDE s TPM

```
    +-----------------------+
    |   Uživatel zapne PC   |
    +----------+------------+
               ↓
    +----------+------------+
    | Bootloader + TPM ověření|
    +----------+------------+
               ↓
    |  TPM uvolní šifrovací klíč  |
               ↓
    +----------+------------+
    | Dešifrování systémového disku |
    +----------+------------+
               ↓
    |    OS se normálně spustí    |
```

TPM (Trusted Platform Module) ukládá šifrovací klíč bezpečně a umožňuje jeho vydání jen při splnění integrity systému (např. nezměněný bootloader, BIOS).

---

### ✅ Ověřování a správa klíčů

- **Hesla vs klíčové soubory** – klíčový soubor může být bezpečnější (např. uložen na USB)
- **Vícefázové odemykání** – např. heslo + klíč na USB
- **Záloha klíčů** – offline, ve fyzickém trezoru

---

### 🧪 Testování a obnova

- **Zálohuj metadata (např. LUKS header)** – umožňuje obnovu
- Testuj obnovu ze šifrovaného média – například obnovením image v sandboxu
- Pokud používáš VeraCrypt, vytvoř záchranný disk (rescue disk)

---

### ❗ Co šifrování neřeší

- Nechrání před malwarem a ransomwarem **během běhu systému**
- Nezabrání úniku dat, pokud uživatel data sám sdílí
- Není náhradou za správu přístupových práv, audit a zálohování

📌 Šifrování je **poslední vrstva**, ne jediná ochrana.

---

### 📚 Citace (Harvard)

- Schneier, B. (2015). *Data and Goliath: The Hidden Battles to Collect Your Data and Control Your World*. Norton & Company.  
- NIST (2020). *FIPS 197: Advanced Encryption Standard (AES)*. Available at: https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.197.pdf  
- VeraCrypt (2024). *Documentation*. Available at: https://www.veracrypt.fr/en/Documentation.html  
- Microsoft (2024). *BitLocker Overview*. Available at: https://learn.microsoft.com/en-us/windows/security/information-protection/bitlocker/bitlocker-overview  
- Linux Foundation (2023). *LUKS/dm-crypt project*. Available at: https://gitlab.com/cryptsetup/cryptsetup

