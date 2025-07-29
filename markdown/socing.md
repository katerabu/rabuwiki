---
title: Sociální inženýrství (Social Engineering)
category: Počítače
tags: [internet, socialní, inženýring, ochrana, kyberbezpečnost]
last_update: 2025-07-29
---

## 🕵️‍♂️ Sociální inženýrství (Social Engineering)

### 🤔 Co je sociální inženýrství?

Sociální inženýrství je technika manipulace s lidmi, jejímž cílem je získat důvěrné informace, přístup nebo způsobit určitou akci. Nezáleží na síle hesla, pokud útočník přesvědčí člověka, aby ho prozradil.

> “The weakest link in the security chain is the human.”  
> – Mitnick, K. (2002). *The Art of Deception*

---

### 🧪 Typy útoků sociálního inženýrství

```
    +-------------------------------+
    |      Nejčastější techniky     |
    +-------------------------------+
    | 📧 Phishing                   |
    | 📱 Vishing (hlasové volání)   |
    | 💬 Smishing (SMS podvody)     |
    | 🎣 Spear phishing             |
    | 🎁 Pretexting (falešný scénář)|
    | 📦 Baiting (nástražný flashdisk)|
    | 🧍 Tailgating (vstup do budovy)|
    +-------------------------------+
```

| Typ útoku         | Popis |
|-------------------|-------|
| **Phishing**       | Podvodné e-maily imitující např. banku |
| **Spear phishing** | Cílený phishing na konkrétní osobu |
| **Pretexting**     | Útočník si vymyslí důvěryhodný příběh |
| **Baiting**        | Flashdisk „nalezený“ v okolí firmy |
| **Vishing**        | Telefonát s cílem vylákat informace |
| **Smishing**       | SMS s odkazem na škodlivý web |
| **Tailgating**     | Neoprávněný vstup za oprávněnou osobou |

---

### 🎭 Příklady z praxe

- USB flashdisk vydávající se za **klávesnici** – po připojení simuluje zadávání příkazů (tzv. BadUSB)
- Nabíjecí kabel s integrovaným **Wi-Fi čipem** pro vzdálené ovládání zařízení
- Podvodný telefonát z „banky“, který tlačí na strach nebo čas

📌 Lidé jsou zranitelní, když jsou pod tlakem: spěch, panika, autorita, zvědavost, pomoc

---

### 🧰 Ochrana proti sociálnímu inženýrství

| Opatření                         | Doporučení |
|----------------------------------|------------|
| 🎓 Školení a osvěta              | Pravidelné simulace phishingu |
| 🧠 Kritické myšlení              | Nedůvěřuj nevyžádaným žádostem |
| 🛠️ MFA                          | I při prozrazení hesla zabrání přístupu |
| 🔌 Nepřipojuj neznámá zařízení  | Flashdisk = vektor útoku |
| 👁️‍🗨️ Fyzická bezpečnost         | Vstupy do budov, hosté, zamčené PC |
| 🔒 Minimální oprávnění          | Princip „nejmenších práv“ (least privilege) |

---

### 🧭 ASCII schéma – Fáze útoku sociálního inženýrství

```
        +------------------------+
        |    1. Průzkum         |
        |  (sběr informací)     |
        +----------+------------+
                   ↓
        +----------+------------+
        |   2. Navázání důvěry  |
        | (např. přes LinkedIn) |
        +----------+------------+
                   ↓
        +----------+------------+
        |   3. Útok               |
        | (např. phishing e-mail)|
        +----------+------------+
                   ↓
        +----------+------------+
        |   4. Získání přístupu |
        | (heslo, přístup do sítě) |
        +----------+------------+
                   ↓
        +----------+------------+
        |   5. Únik dat / škoda |
        +------------------------+
```

---

### 📚 Citace a doporučená literatura

- Mitnick, K.D. (2002). *The Art of Deception: Controlling the Human Element of Security*. Wiley.
- Hadnagy, C. (2021). *Human Hacking: Win Friends, Influence People, and Leave Them Better Off*. Harper Business.
- CISA (2022). *Social Engineering Tactics*. Available at: https://www.cisa.gov/news-events/news/protect-against-social-engineering  
- SANS Institute (2023). *Phishing Simulation Toolkit*. https://www.sans.org/security-awareness-training/phishing/
- CERT-EU (2024). *Threat Landscape Report – Human Exploitation Techniques*. https://cert.europa.eu

---

### 🛑 Pamatuj: Největší zbraní útočníka je tvoje důvěra.

Pokud něco vypadá podezřele, zeptej se.  
Pokud někdo spěchá, zdrž ho.  
Pokud máš pochybnosti, **neklikej**.

