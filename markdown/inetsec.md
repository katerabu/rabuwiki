---
title: Internet Security (Bezpečnost webu a sítí)
category: Počítače
tags: [internet, weby, sítě, kryptografie, kyberbezpečnost]
last_update: 2025-07-29
---

## 🌐 Internet Security (Bezpečnost webu a sítí)

### 🧱 Definice a principy
- **Internet Security** pokrývá technická opatření na ochranu dat v přenosu i v klidu (např. šifrování TLS/SSL, VPN, IPsec). Označuje se také jako síťová vrstva ochrany (Van Rossum, 2025). :contentReference[oaicite:1]{index=1}
- Klíčovým konceptem je **Defense in Depth** – více vrstev ochrany: firewall, antivir, šifrování, segmentace sítě, princip nejmenších práv (NSA, 2025). :contentReference[oaicite:2]{index=2}

### 🛡️ Ochrana přenosu a protokoly
- Používej **TLS/SSL** pro webové stránky a email (např. HTTPS, PGP, IPsec), vždy ověř certifikáty. :contentReference[oaicite:3]{index=3}
- Implementuj **VPN nebo segmentaci sítě** (např. VLAN), aby se zabránilo laterálním pohybům útočníků. :contentReference[oaicite:4]{index=4}

### 👤 Přístupová kontrola a IAM
- Aktivuj **Multi-Factor Authentication (MFA)** všude kde je to možné. Podle Infosec (2025) a TechTarget (2025) to zásadně snižuje riziko. :contentReference[oaicite:5]{index=5}
- Dodrž **princip nejmenších práv** (least privilege) – uživatelé a služby mají pouze přístup k tomu, co skutečně potřebují. :contentReference[oaicite:6]{index=6}
- Pravidelně audituj role a účty; zneplatňuj přístupy neaktivním nebo odcházejícím uživatelům. :contentReference[oaicite:7]{index=7}

### 💻 Endpointy & zařízení
- Aktuálnost software je kritická – bezpečnostní záplaty instaluj **do 7 dnů od vydání** (např. podle Penn IS). :contentReference[oaicite:8]{index=8}
- Používej **antivirový software, osobní firewally** a EDR/EPP ochranu na koncových zařízeních. :contentReference[oaicite:9]{index=9}
- Aktivuj **šifrování disku** (např. LUKS, BitLocker), zvláště na mobilních a přenosných zařízeních. :contentReference[oaicite:10]{index=10}

### 📝 Síťový dohled a reakce
- Centralizované logování, monitoring síťového provozu a detailní audit pomáhají detekovat anomálie v reálném čase. :contentReference[oaicite:11]{index=11}
- Proaktivní bezpečnostní přístup: pravidelné testování zranitelností, penetrační testy, simulované útoky a cvičení reakce. :contentReference[oaicite:12]{index=12}

### 🌍 Lidé & kultura bezpečnosti
- Vzdělávání uživatelů zvyšuje odolnost proti phishingu a sociálnímu inženýrství – podle IBM X‑Force v roce 2023 za lidský faktor zodpovídá 95 % incidentů. :contentReference[oaicite:13]{index=13}
- Budování **bezpečnostní kultury** je klíčové — zodpovědnost, hlášení podezřelých událostí, a sankce za porušení politik. :contentReference[oaicite:14]{index=14}

### 📑 Rámce a standardy
- Doporučeným rámcem pro řízení rizik je **NIST CSF** (funkce: Identify, Protect, Detect, Respond, Recover). :contentReference[oaicite:15]{index=15}
- Pro detailní řízení rizik lze aplikovat standard **ISO/IEC 27005** (správa rizik v ISMS v rámci ISO27k). :contentReference[oaicite:16]{index=16}

### 🔗 Doporučené best practices (výběr)
| Praktika | Popis |
|---------|-------|
| Zálohování 3‑2‑1 s air-gapping | Ochrana před ransomwarem – izolace záloh |
| Šifrování v klidu i při přenosu | Ochrana dat bez ohledu na médium |
| Mikrosegmentace a whitelisting | Omezení přístupu na nejméně důvěryhodné prostředí |
| Zero‑Trust přístupové politiky | Nikomu se ve výchozím stavu nevěří; všechno se ověřuje |

---

### 📚 Vybraná literatura a zdroje
- Van Rossum, 2025 – Internet Security a síťové protokoly (TLS, IPsec) :contentReference[oaicite:17]{index=17}  
- TechTarget, 2025 – Strategie „defense in depth“, segmentace, MFA :contentReference[oaicite:18]{index=18}  
- Infosec Institute, 2025 – Role MFA, aktualizací a firewallu :contentReference[oaicite:19]{index=19}  
- PreventiveApproach, 2024 – Síťové best practices, segmentace, NAT, VPN :contentReference[oaicite:20]{index=20}  

---
## 📘 ISO 27001 & ISO/IEC 27002 – Standardy a struktura

### 🏗️ Struktura norm ISO 27000 rodiny
- **ISO/IEC 27000** – přehled a terminologie
- **ISO/IEC 27001:2022** – požadavky na ISMS (Information Security Management System)
- **ISO/IEC 27002:2022** – praktický kódex bezpečnostních opatření (Annex A) :contentReference[oaicite:2]{index=2}

### 🌀 Implementační rámec ISO 27001
- ISMS se zavádí pomocí cyklu **PDCA (Plan–Do–Check–Act)**:
  1. Určení kontextu, zájmových stran, cílový rozsah
  2. Posouzení rizik (asset → threat → vulnerability)
  3. Výběr a nasazení kontrol (Annex A)
  4. Monitorování, audit, zpětná vazba, zlepšování systému :contentReference[oaicite:3]{index=3}

### 🧩 Diagramová ilustrace procesního rámce
Obrázek nahoře zachycuje strukturu normy rozdělenou do tří úrovní:
- **Strategická** — politika, strategie, governance
- **Taktická** — risk management, implementace kontrol
- **Operační** — monitorování, reporting, školení zaměstnanců :contentReference[oaicite:4]{index=4}

### 📄 Klasifikace kapitol ISO 27001:2022
Norma obsahuje **10 hlavních klauzulí** řízení ISMS plus **Annex A** se 93 kontrolami, strukturovanými do čtyř domén:
- Organizační
- Pro lidi
- Fyzická
- Technologická bezpečnost :contentReference[oaicite:5]{index=5}

### 🛠️ Praktická doporučení pro implementaci
- Udržuj dokumentaci **jednoduchou** a srozumitelnou — méně je někdy více :contentReference[oaicite:6]{index=6}
- Implementuj **procesní přístup** — sleduj vstupy, výstupy, cíle (risk → kontrola → akce) :contentReference[oaicite:7]{index=7}
- Můžeš využít dostupné **zdarma toolkit‑y a šablony** jako startovací bod (např. sdílené na Redditu) :contentReference[oaicite:8]{index=8}

### 📚 Souvisící standardy a rámce
- **ISO/IEC 27002:2022** – podpora výběru kontrol dle Annex A (14 kapitol) :contentReference[oaicite:9]{index=9}  
- **ISO/IEC 27005:2018** – management rizik (doporučeno pro analýzu hrozeb)  
- Kompatibilní s **NIST Cybersecurity Framework (CSF)** – provazba mezi ISO a CSF k naplnění governance a compliance požadavků :contentReference[oaicite:10]{index=10}

### 🎯 Shrnutí přínosů standardů ISO

| Výhoda                         | Popis |
|-------------------------------|-------|
| Celostní přístup              | Pokrývá technické, fyzické i personální aspekty bezpečnosti |
| Flexibilita                   | Každá organizace vybírá kontroly podle vlastních rizik |
| Sdílení a porovnání           | Snadné srovnání s jinými rámci jako NIST nebo COBIT |
| Auditovatelná certifikace     | Pasuje do požadavků partnerů / zákazníků či regulátorů |
| Kontinuální zlepšování        | PDCA cyklus podporuje adaptaci na nová rizika |

### 📎 Doporučené odkazy
- Wikipedia: ISO/IEC 27001 – přehled a revize (2022) :contentReference[oaicite:11]{index=11}  
- InfoAdvisera diagramy: rizikový management & implementace krok‑za‑krokem :contentReference[oaicite:12]{index=12}  
- Struktura ISO rodiny: ISO/IEC 27000–27999 přehled :contentReference[oaicite:13]{index=13}

---

*Poznámka: Obrázek zobrazuje rámec strategicko‑takticko‑operační, text byl ověřen dle aktuální verze ISO 27001:2022.*  

## 📗 ISO 27001:2022 – Standard, struktura a ASCII diagram

### 📄 Oficiální odkaz na dokument
- Text ISO/IEC 27001:2022 je oficiálně publikován ISO/IEC a je dostupný k zakoupení jako PDF na [ISO webu]®.  
  - ISO/IEC 27001:2022 – požadavky pro ISMS (publikace říjen 2022) :contentReference[oaicite:1]{index=1}  
  - Existuje i doplňek **Amendment 1: 2024** (např. klimatické změny), dostupný jako aktualizace standardu :contentReference[oaicite:2]{index=2}

### 🏛️ ISO rodina 27000‑27999
Normy v této řadě pokrývají témata jako implementaci, řízení rizik, audit, incident management a cloud bezpečnost:
- ISO/IEC 27000, 27002, 27003, 27005, 27017, 27033 apod. :contentReference[oaicite:3]{index=3}

---

### 🌀 ASCII diagram – PDCA cyklus a přehled klauzulí

    +---------------------------+
    |         Plan              |
    | (Context, Leadership,     |
    |  Risk Assessment &        |
    |  Treatment)              |
    +-----------+---------------+
                ↓
    +-----------+---------------+
    |          Do               |
    | (Implement Controls,      |
    |  Operations – Annex A)    |
    +-----------+---------------+
                ↓
    +-----------+---------------+
    |         Check             |
    | (Monitor, Audit, Metrics, |
    |  Review)                  |
    +-----------+---------------+
                ↓
    +-----------+---------------+
    |         Act               |
    | (Corrective actions,      |
    |  Continual improvement)   |
    +---------------------------+

Pod diagramem závisí aplikace normy přes klauzule 4 až 10:
Clause 4: Context
Clause 5: Leadership
Clause 6: Planning
Clause 7: Support
Clause 8: Operation
Clause 9: Performance evaluation
Clause 10: Improvement
Annex A: 93 kontrol podle čtyř domén

---

### 🧾 Praktická doporučení (ISO & implementace)

- Dodržte úplnost: **všechny klauzule 4–10 jsou povinné** pro deklaraci shody s normou (nelze některé vynechat) :contentReference[oaicite:4]{index=4}  
- Annex A obsahuje soubor **93 kontrol**, které se vybírají na základě rizikové analýzy (např. klauzule 6.1, 8.4 atd.) :contentReference[oaicite:5]{index=5}  
- Součástí standardu je i dokument “Amendment 1: Climate action changes” z roku 2024 :contentReference[oaicite:6]{index=6}

---

### 📚 Doporučené zdroje (Harvard styl)

- ISO/IEC 27001:2022, International Organization for Standardization & IEC, říjen 2022 – požadavky na ISMS :contentReference[oaicite:7]{index=7}  
- ISO/IEC 27001:2022/Amd 1:2024, International Organization for Standardization & IEC, únor 2024 – doplněk změn spojených s klimatickou problematikou :contentReference[oaicite:8]{index=8}  
- ISO Standards listing (ISO family 27000–27999), Wikipedia, poslední revize 2023 :contentReference[oaicite:9]{index=9}  

---

### 🧩 Vložení do GitHub Wiki

```markdown
## ISO 27001:2022 – struktura a ASCII diagram

### Oficiální dokument
- ISO/IEC 27001:2022 – standard k zakoupení (říjen 2022)
- Amendment 1: 2024 – aktualizace standardu

### ASCII diagram PDCA cyklus  
    +---------------------------+
    |         Plan              |
    | (Context, Leadership,     |
    |  Risk Assessment &        |
    |  Treatment)              |
    +-----------+---------------+
                ↓
    +-----------+---------------+
    |          Do               |
    | (Implement Controls,      |
    |  Operations – Annex A)    |
    +-----------+---------------+
                ↓
    +-----------+---------------+
    |         Check             |
    | (Monitor, Audit, Metrics, |
    |  Review)                  |
    +-----------+---------------+
                ↓
    +-----------+---------------+
    |         Act               |
    | (Corrective actions,      |
    |  Continual improvement)   |
    +---------------------------+

### Klauzule normy ISO
- Clauses 4 → 10 + Annex A (93 kontrol)

### Doporučené odkazy (Harvard)
- ISO/IEC 27001:2022 (ISO & IEC, 2022)
- ISO/IEC 27001:2022/Amd 1:2024 (ISO & IEC, 2024)
- ISO family 27000–27999 (Wikipedia, 2023)  
