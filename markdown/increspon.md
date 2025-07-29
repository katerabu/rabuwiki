## 🧯 Incident Response (reakce na bezpečnostní incidenty)

### 🧭 Co je Incident Response?

Incident Response (IR) je strukturovaný a systematický proces, který organizace používá k **identifikaci, analýze a řešení bezpečnostních incidentů**. Cílem je minimalizovat škody, obnovit normální provoz a zabránit opakování incidentů.

> „Preparation and timely response are critical to reduce the impact of cybersecurity incidents.“  
> – NIST SP 800-61 Revision 2 (2012)

---

### 📋 Fáze Incident Response podle NIST

```
+-------------------+
| 1. Preparation    |
+-------------------+
         ↓
+-------------------+
| 2. Detection &    |
|    Analysis       |
+-------------------+
         ↓
+-------------------+
| 3. Containment,   |
|    Eradication &  |
|    Recovery       |
+-------------------+
         ↓
+-------------------+
| 4. Post-Incident  |
|    Activity       |
+-------------------+
```

| Fáze              | Popis                                                        |
|-------------------|--------------------------------------------------------------|
| **Preparation**   | Školení týmů, definice nástrojů a postupů, prevence          |
| **Detection & Analysis** | Identifikace incidentu, určení rozsahu a dopadů           |
| **Containment, Eradication & Recovery** | Zastavení šíření, odstranění příčiny, obnova systémů |
| **Post-Incident Activity** | Vyhodnocení incidentu, dokumentace, zlepšení procesů     |

---

### 🔥 Typy bezpečnostních incidentů

- Malware a ransomware útoky  
- Neoprávněný přístup (průnik)  
- Únik citlivých dat (data breach)  
- Phishingové a sociálně-inženýrské útoky  
- DDoS útoky  
- Fyzická kompromitace zařízení  

---

### 🛠️ Klíčové nástroje a technologie pro Incident Response

| Nástroj                   | Účel                                          |
|---------------------------|-----------------------------------------------|
| SIEM (Security Information and Event Management) | Centralizovaná detekce a korelace událostí  |
| EDR (Endpoint Detection and Response)            | Analýza a reakce na koncových bodech         |
| Forenzní nástroje (FTK, EnCase)                   | Sběr a analýza digitálních důkazů            |
| Sandbox nástroje (Cuckoo Sandbox)                  | Izolace a analýza malware                      |
| Komunikační kanály (ticketing, Slack, email)      | Koordinace týmu a evidence incidentů          |

---

### 🔐 Incident Response pro mobilní flotilu

Mobilní zařízení představují specifické výzvy v oblasti IR díky jejich mobilitě, heterogenním platformám a často BYOD (Bring Your Own Device) scénářům.

#### Klíčové body pro Incident Response mobilních zařízení:

- **Detekce kompromitace:** Monitoring root/jailbreak, neobvyklé chování aplikací a změny konfigurace.  
- **Dálkové zabezpečení:** Možnost rychlého dálkového uzamčení nebo smazání zařízení pomocí MDM nástrojů.  
- **Forenzní zachování dat:** Zajištění integrity dat a logů pro pozdější analýzu.  
- **Oddělení dat:** Jasné rozdělení firemních a osobních dat (sandboxing/profilování).  
- **Reakce na phishing a malware:** Aktivní vzdělávání uživatelů a rychlá blokace škodlivých aplikací.  

---

### 🔄 Příklad procesu Incident Response pro mobilní zařízení

```
+----------------------------+
| Detekce incidentu (MDM/UEM) |
+-------------+--------------+
              ↓
+-------------+--------------+
| Izolace zařízení (remote lock/wipe) |
+-------------+--------------+
              ↓
+-------------+--------------+
| Forenzní sběr a analýza dat  |
+-------------+--------------+
              ↓
+-------------+--------------+
| Obnova a náprava            |
+-------------+--------------+
              ↓
+-------------+--------------+
| Vyhodnocení a zlepšení procesů |
+----------------------------+
```

---

### 📝 Doporučení pro efektivní Incident Response

| Doporučení                      | Důvod                                               |
|--------------------------------|----------------------------------------------------|
| ✅ Vypracovat a pravidelně testovat IR plán | Připravenost na různé typy incidentů               |
| ✅ Pravidelně školit zaměstnance | Prevence a rychlá reakce na sociální inženýrství   |
| ✅ Používat monitoring a SIEM/EDR | Včasná detekce a rychlá reakce                       |
| ✅ Zálohovat data a používat šifrování | Rychlá obnova a ochrana integrity dat               |
| ✅ Definovat jasné role a odpovědnosti | Efektivní koordinace týmu při incidentu              |

---

### 📚 Důležité standardy a doporučení

- **NIST SP 800-61 Revision 2 (2012)** – *Computer Security Incident Handling Guide*  
  [🔗 https://doi.org/10.6028/NIST.SP.800-61r2](https://doi.org/10.6028/NIST.SP.800-61r2)  
- **ISO/IEC 27035:2016** – *Information security incident management*  
  [🔗 https://www.iso.org/standard/60803.html](https://www.iso.org/standard/60803.html)  
- **SANS Incident Handler’s Handbook**  
  [🔗 https://www.sans.org/reading-room/whitepapers/incident/incident-handlers-handbook-33901](https://www.sans.org/reading-room/whitepapers/incident/incident-handlers-handbook-33901)

---

### 📚 Citace (Harvard)

- NIST (2012). *SP 800-61 Revision 2 – Computer Security Incident Handling Guide*.  
- ISO (2016). *ISO/IEC 27035:2016 – Information security incident management*.  
- SANS Institute (2020). *Incident Handler’s Handbook*. Available at: https://www.sans.org/reading-room/whitepapers/incident/incident-handlers-handbook-33901  
- Gartner (2023). *Magic Quadrant for Security Information and Event Management*.  

