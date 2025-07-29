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

---

Pokud chceš, můžu připravit další související témata jako:

- 🛡️ Forenzní analýza cloudových prostředí  
- ⚙️ Automatizace forenzních procesů  
- 🔒 Právní aspekty digitální forenzní analýzy  

Stačí říct!
