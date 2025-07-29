---
title: Zabezpečení prohlížečů a soukromí online
category: Počítače
tags: [linux, browser, internet, kyberbezpečnost]
last_update: 2025-07-29
---

## 🌐 Zabezpečení prohlížečů a soukromí online

Prohlížeče jsou hlavní branou na internet, kde dochází k citlivým operacím – přihlašování, nákupům, práci s osobními údaji. Zabezpečení prohlížečů a ochrana soukromí jsou proto zásadní.

---

### 🔐 Základní bezpečnostní nastavení prohlížeče

- **Aktualizace prohlížeče:** Pravidelně aktualizuj prohlížeč, aby byly opraveny bezpečnostní chyby a zranitelnosti.  
- **Blokování vyskakovacích oken a reklam:** Aktivuj blokování reklam (např. pomocí rozšíření jako uBlock Origin).  
- **Používání HTTPS:** Kontroluj, že navštěvované weby používají HTTPS (zámek v adresním řádku).  
- **Omezení cookies:** Nastav prohlížeč tak, aby blokoval třetí strany cookies a omezoval sledování.

---

### 🕵️‍♂️ Ochrana soukromí

- **Používání režimu anonymního / soukromého prohlížení:** Nebere historii ani cookies po ukončení relace.  
- **Vymazání historie a cookies:** Pravidelně mazej historii, cache a cookies.  
- **Použití rozšíření na ochranu soukromí:** Například Privacy Badger, Ghostery nebo HTTPS Everywhere.  
- **Blokování sledovacích skriptů:** Použij uBlock Origin nebo NoScript (pro pokročilé uživatele).  
- **Používání vyhledávačů zaměřených na soukromí:** DuckDuckGo, Startpage.

---

### 🔒 Správa hesel a přihlašování

- **Nepoužívej uložená hesla v prohlížeči, pokud možno:** Lepší je používat specializované správce hesel (Bitwarden, 1Password).  
- **Nepoužívej „Přihlásit se pomocí Google/Facebook“ pro důležité služby:** Zvyšuješ tak sdílení dat třetím stranám.  
- **Zapni dvoufaktorové ověřování (2FA):** Pro všechny důležité služby.

---

### ⚙️ Pokročilé zabezpečení a nastavení

- **Zakázání automatického spouštění pluginů:** Zabraňuje spuštění škodlivých skriptů (např. Flash, Java).  
- **Používání kontejnerů (Firefox Multi-Account Containers):** Izoluje aktivitu různých webů pro omezení sledování.  
- **Sandboxing prohlížeče:** Používej prohlížeče s bezpečnostními sandboxy (Chrome, Edge, Firefox).  
- **Nastavení Content Security Policy (CSP):** Uživatelé i vývojáři by měli znát, jak weby omezují zdroje a skripty.

---

### 🌐 VPN a anonymní prohlížení

- Používání VPN skrývá IP adresu a šifruje data při přístupu k internetu.  
- Pro anonymní prohlížení lze použít Tor Browser (ale s omezeními rychlosti a kompatibility).

---

### 🛠️ Praktické návody pro zabezpečení jednotlivých prohlížečů

#### Google Chrome

1. **Aktualizace:**  
   - Menu (tři tečky) → „Nápověda“ → „O Chromu“ → automatická aktualizace.  
2. **Blokování reklam a sledování:**  
   - Nainstaluj rozšíření [uBlock Origin](https://ublockorigin.com/) a [Privacy Badger](https://privacybadger.org/).  
3. **Správa cookies:**  
   - Nastavení → „Soukromí a zabezpečení“ → „Cookies a jiná data webu“ → „Blokovat třetí strany cookies“.  
4. **Správa hesel:**  
   - Nastavení → „Automatické vyplňování“ → „Správce hesel“. Doporučuje se ale používat externí správce hesel.

#### Mozilla Firefox

1. **Aktualizace:**  
   - Menu (tři čáry) → „Nápověda“ → „O Firefoxu“.  
2. **Použití kontejnerů:**  
   - Nainstaluj [Firefox Multi-Account Containers](https://addons.mozilla.org/en-US/firefox/addon/multi-account-containers/).  
3. **Ochrana soukromí:**  
   - Nastavení → „Soukromí a zabezpečení“ → povolit „Blokování sledování obsahu“ (nastavit na „Přísné“ nebo „Vlastní“).  
4. **Rozšíření:**  
   - Doporučená: uBlock Origin, Privacy Badger, HTTPS Everywhere.  
5. **Správa hesel:**  
   - Nastavení → „Účty Firefoxu“ → „Přihlašovací údaje a hesla“.  
   - Pro vyšší bezpečnost používej externí správce hesel.

#### Microsoft Edge

1. **Aktualizace:**  
   - Menu (tři tečky) → „Nápověda a zpětná vazba“ → „O aplikaci Microsoft Edge“.  
2. **Soukromí:**  
   - Nastavení → „Ochrana soukromí, vyhledávání a služeb“ → „Blokování sledování“ → nastav na „Striktní“.  
3. **Rozšíření:**  
   - Umožni rozšíření z Chrome Web Store, nainstaluj uBlock Origin, Privacy Badger.  
4. **Správa hesel:**  
   - Nastavení → „Profily“ → „Hesla“.

---

### 💡 Další praktické tipy

- **Pravidelně čistit cache, cookies a historii:** Pomáhá omezit sledování a uvolňuje místo.  
- **Nepoužívat stejná hesla napříč weby:** Minimalizuje riziko kompromitace více účtů.  
- **Vyhýbat se podezřelým webům a odkazům:** Phishingové a malware stránky často maskované za legitimní.  
- **Používat správce hesel:** Usnadňuje tvorbu a správu unikátních a silných hesel.  
- **Zálohovat důležitá data z prohlížeče:** Export záložek, nastavení.  
- **Vypnout ukládání hesel v prohlížeči, pokud používáš správce hesel.**  
- **Použít HTTPS-Only režim:** Např. v Firefoxu v nastavení Soukromí → Zapnout vždy HTTPS.  
- **Používat rozšíření jako NoScript na kritických zařízeních:** Omezuje spouštění JavaScriptu a pluginů, které mohou být zneužity.  
- **Deaktivovat automatické přihlášení:** Předejde nepovolenému přístupu, pokud se zařízení dostane do rukou třetím osobám.

---

### 📚 Citace (Harvard)

- OWASP Foundation (2023). *OWASP Top 10 Web Application Security Risks*. [online] Available at: https://owasp.org/www-project-top-ten/ [Accessed 2025].  
- Electronic Frontier Foundation (2024). *Surveillance Self-Defense*. [online] Available at: https://ssd.eff.org/ [Accessed 2025].  
- Mozilla Foundation (2024). *Firefox Privacy Notice*. [online] Available at: https://www.mozilla.org/en-US/privacy/firefox/ [Accessed 2025].

---

### 🔗 Uživatelské návody a zdroje

- [Mozilla Firefox Security Settings](https://support.mozilla.org/en-US/kb/firefox-security-settings)  
- [Google Chrome Privacy and Security Settings](https://support.google.com/chrome/answer/114836)  
- [Privacy Badger](https://privacybadger.org/)  
- [uBlock Origin](https://ublockorigin.com/)  
- [Tor Project](https://www.torproject.org/)

