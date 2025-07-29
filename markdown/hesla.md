## 🔐 Hesla a autentizace

### 🧠 Základní principy

Autentizace je proces ověření identity uživatele. V běžné praxi jde o kombinaci něčeho, co **znáš** (heslo), **máš** (telefon, token) nebo **jsi** (biometrie).

Heslo je nejčastější, ale zároveň nejslabší metoda. Špatně vytvořené nebo opakovaně použité heslo bývá nejsnazším cílem útoků jako jsou:

- Slovníkový útok (*dictionary attack*)
- Hrubá síla (*brute-force*)
- Phishing
- Úniky z databází třetích stran

---

### 📋 Doporučené zásady pro hesla

| Doporučení                            | Poznámka |
|--------------------------------------|----------|
| ✅ Používej **dlouhé heslové fráze** | min. 16+ znaků, např. "mokrá‑židle‑tráva‑kostka" |
| ✅ Nepoužívej stejné heslo vícekrát  | Unikátní pro každý účet |
| ✅ Nepamatuj si je – **používej správce hesel** | Viz níže |
| ✅ Zapni **dvoufázové ověření (MFA)** | Např. TOTP, U2F, push notifikace |
| ❌ Nepoužívej jména, data narození, qwerty, 123456 | Snadno uhodnutelné |
| ❌ Nepřihlašuj se pomocí „Sign in with Google / FB“ | Může narušit oddělení identit |

---

### 🔑 Správci hesel (password managers)

| Nástroj        | Typ       | Poznámka |
|----------------|-----------|----------|
| **Bitwarden**  | Open-source, cloud / self-hosted | End-to-end šifrování |
| **KeePassXC**  | Offline    | Ukládá do .kdbx, ideální pro paranoidní uživatele |
| **1Password**  | Komerční   | Silná MFA, integrace s firmami |
| **Pass (Linux)** | CLI-based | GPG šifrování, Unix-friendly |

📌 Hlavní heslo správce: použij **dlouhou unikátní frázi**, např. 6–8 náhodných slov

---

### 🛡️ Dvoufaktorová autentizace (2FA/MFA)

```
    +-----------------------------+
    |     MFA – 3 faktory        |
    +-----------------------------+
    | 1. Něco, co ZNÁŠ            |
    |    (heslo, PIN)             |
    | 2. Něco, co MÁŠ             |
    |    (telefon, token, YubiKey)|
    | 3. Něco, čím JSI            |
    |    (otisk, obličej)         |
    +-----------------------------+
```

| Typ MFA       | Příklady |
|---------------|----------|
| **TOTP (časové kódy)** | Google Authenticator, Authy, Aegis |
| **Push notifikace**    | Duo, Okta, Microsoft Authenticator |
| **Fyzické klíče**      | YubiKey, SoloKey (FIDO2 / U2F) |
| **Biometrie**          | Otisk, Face ID, Windows Hello |

📌 Nejbezpečnější: **fyzický bezpečnostní klíč** (FIDO2) + silné heslo

---

### 🔍 Jak funguje ověřovací aplikace (např. TOTP)

1. Při aktivaci MFA se vygeneruje sdílený tajný klíč (QR kód).
2. Ten je uložen v aplikaci (např. Aegis).
3. Algoritmus HMAC s časovým razítkem generuje každých 30 sekund nové číslo.
4. Server ověří, zda kód odpovídá očekávanému časovému oknu.

Standard: **RFC 6238** (TOTP) a **RFC 4226** (HOTP)  
Ověřitelné např. open-source knihovnou: [pyotp](https://pyauth.github.io/pyotp/)

---

### 🧰 Nástroje pro testování hesel

- **Have I Been Pwned** – zjistí, zda se heslo objevilo v úniku: https://haveibeenpwned.com  
- **Zxcvbn** – knihovna pro měření síly hesla od Dropboxu  
- **CrackStation** – seznam běžně cracknutelných hesel: https://crackstation.net  

---

### 📚 Citace (Harvard)

- Vacca, J.R. (2020). *Computer and Information Security Handbook*. 3rd ed. Elsevier.  
- NIST (2020). *SP 800-63B: Digital Identity Guidelines*. Available at: https://pages.nist.gov/800-63-3/sp800-63b.html  
- Hunt, T. (2024). *Have I Been Pwned?*. Available at: https://haveibeenpwned.com  
- Dropbox (2021). *Zxcvbn: realistic password strength estimator*. GitHub repo: https://github.com/dropbox/zxcvbn  
- RFC 6238: *TOTP – Time-Based One-Time Password Algorithm*. IETF.  
