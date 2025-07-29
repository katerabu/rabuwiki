## 🔍 Forenzní analýza a auditování

### 🧩 Co je Forenzní analýza?

Digitální forenzní analýza je proces **sběru, uchování, analýzy a prezentace digitálních důkazů** tak, aby byly použitelné v rámci vyšetřování bezpečnostních incidentů, porušení politik nebo i soudních sporů.

> „Digital forensics is the practice of uncovering and interpreting electronic data.“  
> – Carrier, B. (2003), *Digital Forensic Research*

---

### 📋 Hlavní kroky digitální forenzní analýzy

```
+-------------------+
| 1. Identifikace   |
+-------------------+
         ↓
+-------------------+
| 2. Zachycení      |
+-------------------+
         ↓
+-------------------+
| 3. Analýza        |
+-------------------+
         ↓
+-------------------+
| 4. Prezentace     |
+-------------------+
```

| Fáze               | Popis                                                   |
|--------------------|---------------------------------------------------------|
| **Identifikace**   | Určení zařízení a dat relevantních k incidentu           |
| **Zachycení**      | Forenzní kopie dat s dodržením integrity a chain-of-custody |
| **Analýza**        | Podrobná zkoumání dat za účelem nalezení důkazů          |
| **Prezentace**     | Vypracování zpráv a případná svědecká výpověď            |

---

### 🛠️ Nástroje a techniky forenzní analýzy

| Nástroj                  | Popis                                             |
|--------------------------|--------------------------------------------------|
| FTK (Forensic Toolkit)   | Kompletní sada pro forenzní vyšetřování          |
| EnCase                   | Populární komerční forenzní software              |
| Autopsy/Sleuth Kit       | Open-source forenzní nástroje                      |
| Volatility               | Analýza paměti (RAM)                               |
| Wireshark                | Analýza síťových dat                               |

---

### 📝 Auditování v kontextu forenzní analýzy

Auditování je **kontinuální proces monitorování a vyhodnocování bezpečnostních opatření**, který podporuje včasnou detekci incidentů a usnadňuje forenzní vyšetřování.

- Záznamy (logy) musí být zabezpečené a neměnné.  
- Pravidelné kontroly integrity dat.  
- Shoda s normami (např. ISO/IEC 27001, PCI DSS).  

---

### 🔍 Forenzní analýza mobilních zařízení

Mobilní zařízení představují specifické výzvy díky omezené možnosti přístupu k datům, různorodým platformám a rychlé změně obsahu.

#### Klíčové aspekty forenzní analýzy mobilů:

- **Zachování integrity dat:** Použití fyzické izolace (např. Faradayova klec), režimu letadlo, aby se zabránilo dálkovému smazání nebo změně.  
- **Získání dat:** Fyzická kopie paměti, logy aplikací, SMS, hovory, GPS data, cloudové zálohy.  
- **Nástroje pro analýzu:** Cellebrite, Oxygen Forensic Detective, MSAB XRY.  
- **Právní aspekty:** Dodržování zákonných pravidel pro sběr a uchovávání dat (např. GDPR).  

---

### 🔄 Proces forenzní analýzy mobilních zařízení

```
+----------------------------+
| 1. Zajištění a izolace     |
+-------------+--------------+
              ↓
+-------------+--------------+
| 2. Extrakce dat            |
+-------------+--------------+
              ↓
+-------------+--------------+
| 3. Analýza dat             |
+-------------+--------------+
              ↓
+-------------+--------------+
| 4. Dokumentace a zpráva    |
+----------------------------+
```

---

### 📚 Doporučení a best practices

- Používat certifikované forenzní nástroje.  
- Dodržovat postupy chain-of-custody.  
- Zajistit bezpečné uchování a zálohování dat.  
- Pravidelně aktualizovat znalosti a nástroje.  

---

### 📚 Standardy a normy

- **ISO/IEC 27037:2012** – Guidelines for identification, collection, acquisition and preservation of digital evidence  
  [🔗 https://www.iso.org/standard/44381.html](https://www.iso.org/standard/44381.html)  
- **ISO/IEC 27041:2015** – Guidance on assuring suitability and adequacy of incident investigative methods  
  [🔗 https://www.iso.org/standard/44382.html](https://www.iso.org/standard/44382.html)  
- **NIST SP 800-86** – Guide to Integrating Forensic Techniques into Incident Response  
  [🔗 https://doi.org/10.6028/NIST.SP.800-86](https://doi.org/10.6028/NIST.SP.800-86)  

---

### 📚 Citace (Harvard)

- Carrier, B. (2003). *Digital Forensic Research: The Next 10 Years*.  
- ISO (2012). *ISO/IEC 27037:2012 – Guidelines for identification, collection, acquisition and preservation of digital evidence*.  
- NIST (2006). *SP 800-86 – Guide to Integrating Forensic Techniques into Incident Response*.  
- Casey, E. (2011). *Digital Evidence and Computer Crime*.  

## 🔍 Forenzní analýza a auditování - I. doplnění 

Forenzní analýza je klíčovou součástí bezpečnostních incidentů, auditů a vyšetřování kybernetických útoků. Cílem je shromáždit, analyzovat a zabezpečit digitální důkazy tak, aby byly použitelné v rámci interních vyšetřování i právních procesů.

---

### 🛡️ Forenzní analýza cloudových prostředí

Cloudové služby přinášejí specifická rizika a výzvy pro forenzní analýzu:

- **Sběr důkazů:** Oproti fyzickým zařízením chybí přímý přístup ke hardwaru, důkazy jsou často distribuované mezi více datovými centry.  
- **Logování a auditní stopy:** Závisí na poskytovateli cloudu a konfiguraci služeb (např. AWS CloudTrail, Azure Monitor).  
- **Kontrola integrity dat:** Nutné používat kryptografické hashe, auditní protokoly a časové razítka.  
- **Spolupráce s poskytovatelem:** Využívání API a požadavky na data musí být koordinovány podle smluvních podmínek a právních rámců.  
- **Zabezpečení multi-tenancy:** Nutnost zajistit oddělení dat a důkazů od ostatních zákazníků.  

Doporučené postupy:  
- Aktivace auditních protokolů ještě před incidentem.  
- Používání nástrojů pro automatizovanou analýzu cloudových logů.  
- Zálohování a export klíčových dat v souladu s GDPR a dalšími regulacemi.

---

### ⚙️ Automatizace forenzních procesů

Automatizace výrazně zvyšuje efektivitu a přesnost forenzních vyšetřování:

- **Nástroje:** Volání skriptů a workflow v nástrojích jako Autopsy, Volatility, GRR Rapid Response, TheHive, Velociraptor.  
- **Automatizované sbírání dat:** Nasazení agentů na systémy pro rychlé zachycení dat při incidentu.  
- **Analýza logů:** Použití SIEM systémů (Splunk, ELK Stack) pro korelaci a rychlou identifikaci vzorců chování.  
- **Reportování:** Automatizovaná generace přehledů a zpráv pro management a právní oddělení.  

Výhody:  
- Minimalizace lidských chyb.  
- Rychlejší reakční doba.  
- Lepší škálovatelnost vyšetřování.

---

### 🔒 Právní aspekty digitální forenzní analýzy

Forenzní analýza se musí řídit zákonnými normami, aby důkazy byly použitelné a nezpochybnitelné:

- **Řetězec důkazů (Chain of Custody):** Dokumentace o původu, manipulaci a uchování digitálních důkazů.  
- **Soulad s legislativou:** GDPR, zákony o ochraně osobních údajů, zákony o kybernetické bezpečnosti a trestním řízení.  
- **Práva a povinnosti vyšetřovatelů:** Potřeba povolení (soudní příkaz) pro přístup k datům, respektování práv uživatelů a obviněných.  
- **Zabezpečení dat:** Zajištění důkazů proti neoprávněné manipulaci či zveřejnění.  
- **Admissibilita důkazů:** Důkazy musí být získány zákonně, nesmí být získány nelegálním způsobem.  

Doporučené kroky:  
- Školení forenzních analytiků v právních otázkách.  
- Používání certifikovaných nástrojů a postupů.  
- Pravidelné audity a revize procesů.

---

### 🔗 Užitečné odkazy

- [NIST Special Publication 800-101 Revision 1 – Guidelines on Mobile Device Forensics](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-101r1.pdf)  
- [ISO/IEC 27037:2012 – Guidelines for identification, collection, acquisition and preservation of digital evidence](https://www.iso.org/standard/44381.html)  
- [SANS Digital Forensics and Incident Response Resources](https://www.sans.org/digital-forensics-and-incident-response/)  
- [Forensic Focus – Community and Resources](https://www.forensicfocus.com/)  

---

### 📚 Citace (Harvard)

- NIST (2014). *Guidelines on Mobile Device Forensics*.  
- ISO (2012). *ISO/IEC 27037:2012 – Guidelines for identification, collection, acquisition and preservation of digital evidence*.  
- SANS Institute (2023). *Digital Forensics and Incident Response Resources*.  
- Casey, E. (2011). *Digital Evidence and Computer Crime: Forensic Science, Computers and the Internet*. 3rd ed. Academic Press.


