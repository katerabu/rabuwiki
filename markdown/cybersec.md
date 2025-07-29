# 🛡️ Cybersecurity – Přehled doporučení a hrozeb

## 📡 Domácí síť a routery

- **Uzamknout přístup ke správě routeru přes Wi-Fi**
  - Vypni vzdálenou správu (remote admin)
  - Používej kabel pro správu nebo whitelist IP adres
  - Změň výchozí hesla a přihlašovací jméno

- **Použít silné a složité heslo k Wi-Fi AP**
  - Použij WPA3, případně WPA2 s dlouhou frází (alespoň 16 znaků)
  - Nepoužívej jméno nebo adresu v SSID

- **Mazat uložené Wi-Fi sítě**
  - Staré sítě mohou být zneužity (tzv. evil twin útoky)
  - Např. přes `Settings > Wi-Fi > Known Networks` ve Windows

---

## 🔒 Přihlašování a ověřování

- **Dvoufázové ověření (2FA) – např. Google Authenticator**
  - Ověřovací aplikace generují časově omezené kódy (TOTP)
  - Doporučené appky: [Google Authenticator](https://play.google.com/store/apps/details?id=com.google.android.apps.authenticator2), [Authy](https://authy.com), [Aegis](https://getaegis.app)
  - Nikdy neukládej záložní kódy nezabezpečeně

- **Používat dlouhou přístupovou frázi pro odemknutí správce hesel**
  - Délka je důležitější než složitost
  - Např.: `Můj_úžasný_správce_hesel_je_bezpečný_123!`

- **Nepoužívat "Přihlásit se pomocí Google/Facebook"**
  - Centralizuje přístup → větší riziko kompromitace
  - Nedostatek kontroly nad oprávněními

---

## 📲 Mobilní a osobní zařízení

- **Herní elektroniku dětem nedarovat, ale půjčovat**
  - Umožňuje zachovat rodičovskou kontrolu a pravidla
  - Pomáhá budovat digitální odpovědnost

- **Signal místo WhatsAppu**
  - Signal je open source a neukládá metadata (vhodnější pro soukromí)
  - Více o srovnání: [Secure Messaging Comparison by EFF](https://www.eff.org/pages/secure-messaging-scorecard)

- **Zabezpečující aplikace pro Android**
  - Např. [Bitdefender Mobile Security](https://www.bitdefender.com/solutions/mobile-security-android.html)
  - Další: Norton, Kaspersky, Avast Mobile Security

---

## 🧠 Sociální inženýrství

- **Typy útoků**:
  - Phishing (e-mail, SMS)
  - Vishing (hlasové podvody)
  - Baiting (návnady, např. flash disk na zemi)
  - Pretexting (vydávání se za autoritu)

- **Příklad: Flashdisk se může chovat jako klávesnice**
  - Útoky typu "Rubber Ducky"
  - Vloží skripty a zadá je jako by byly psané klávesnicí

- **Kabel k nabíječce může fungovat jako Wi-Fi AP**
  - Např. **OMG Cable** – upravený USB kabel s vestavěným čipem
  - Viz [https://mg.lol/blog/omg-cable/](https://mg.lol/blog/omg-cable/)

---

## 🌐 Web, odkazy a prohlížeče

- **Zkrácené odkazy – přidáním `+` zjistíš cílovou adresu**
  - Např.: `bit.ly/xyz123+`
  - Ověříš před kliknutím, kam vede

- **Mazat staré záložky bez kontroly obsahu**
  - Doména může být prodána a vést na škodlivý obsah

- **Nepoužívat SSD pro zálohování – proč?**
  - SSD nemají garantovanou datovou retenci bez napájení
  - HDD (3.5") a optická média jako [M-DISC](https://www.verbatim.com/subcat/optical-media/m-disc/) jsou lepší na dlouhodobé uložení

---

## 🧯 Zálohování

- **Používej zálohovací strategii 3-2-1**
  - 3 kopie dat
  - 2 různá média
  - 1 mimo pracovní prostor (např. externí disk mimo domov)

- **Zálohy nešifrovat (v některých scénářích)**
  - U důležitých záloh může být výhodnější čitelnost bez softwaru

- **Zálohovat na 3,5" HDD nebo M-DISC**
  - Nejodolnější média pro archivní uložení
  - M-DISC garantuje uchování dat až 1 000 let (dle výrobce)

---

## 💻 Práce s počítačem

- **Zaheslování pracovní stanice s Linuxem**
  - Použij LUKS pro šifrování disku + heslo k systému
  - Heslo uložit do zalepené obálky v trezoru

- **U malých zařízení (např. Raspberry Pi)**:
  - Vymazat historii prohlížeče a uložená hesla
  - V prohlížeči (např. Firefox, Chromium) nastav:
    - Nepamatovat historii (`Nastavení > Soukromí > Nepamatovat si historii`)
    - Zakázat ukládání hesel

---

## 🔐 Ochrana osobních údajů

- **Neukládat platební karty v e-shopu**
  - Při úniku dat může být zneužita
  - Případně používat virtuální kartu (např. Revolut, Apple Pay)

- **Nechlubit se nastavením zabezpečení**
  - Můžeš se stát cílem (např. motivace útočníků)
  - Platí zásada: „bezpečnost je jako cibule – vrstvy a diskrétnost“

- **Zveřejňování přes messengery = veřejná komunikace**
  - Data mohou být uchovávána, analyzována nebo zneužita
  - Věř pouze end-to-end šifrovaným aplikacím (např. Signal)
  - Citace: „Anything you send online can be made public – assume it will.“

---

## 📚 Citace a odkazy

- [EFF Secure Messaging Guide](https://www.eff.org/pages/secure-messaging-scorecard)
- [Google Authenticator](https://play.google.com/store/apps/details?id=com.google.android.apps.authenticator2)
- [OMG Cable – Wi-Fi útoky přes kabel](https://mg.lol/blog/omg-cable/)
- [Bitdefender Mobile Security](https://www.bitdefender.com/solutions/mobile-security-android.html)
- [M-DISC archivní média](https://www.verbatim.com/subcat/optical-media/m-disc/)

---

*Autor poznámek: školení Cybersecurity – přeformátováno a doplněno AI.*
