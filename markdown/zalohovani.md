---
title: Zálohování a obnova dat (Backup & Recovery)
category: Počítače
tags: [backup, recovevry, kyberbezpečnost]
last_update: 2025-07-29
---

## 💾 Zálohování a obnova dat (Backup & Recovery)

### 📘 Co je zálohování?
Zálohování je proces kopírování dat do jiného umístění za účelem jejich obnovy v případě ztráty, poškození nebo kybernetického útoku (např. ransomware).

> „There are two kinds of people: those who back up, and those who have never lost all their data yet.“  
> – Phil Karlton (cit. v Vacca, 2020)

---

### 🔁 Základní strategie: Pravidlo 3–2–1

```
        +-----------------------------+
        |         PRAVIDLO 3–2–1     |
        +-----------------------------+
        | 3 kopie dat                 |
        | 2 různá média               |
        | 1 kopie off-site (mimo firmu) |
        +-----------------------------+
```

- **3 kopie**: originál + 2 záložní kopie  
- **2 různá média**: např. disk + páska, nebo NAS + cloud  
- **1 mimo lokalitu**: pro případ požáru, krádeže, ransomwaru  

📌 Doplněk: Pravidlo **3–2–1–1–0**  
- +1 offline (air-gap)  
- +0 chyb ve verifikaci (test obnovy)  

Zdroj: Veeam (2023), NIST (2021)

---

### 🗂️ Typy záloh

| Typ            | Popis |
|----------------|-------|
| **Full**       | Celá kopie dat; pomalé, velké |
| **Incremental**| Jen změny od poslední zálohy |
| **Differential**| Vše změněné od poslední **plné** zálohy |

📌 Doporučeno: denní **inkrementální**, týdenní **plná**

---

### 🗃️ Typy úložišť

| Úložiště         | Výhody / Nevýhody |
|------------------|-------------------|
| **Externí HDD**  | Dostupné, ale méně spolehlivé pro dlouhodobou archivaci |
| **3,5" disky**   | Vyšší odolnost, vhodné pro studené zálohy |
| **NAS**          | Centralizované, podporuje verze |
| **Cloud**        | Rychlý přístup, ale dražší při obnově |
| **Magnetická páska** | Odolnost >30 let, vhodné pro offline |

📌 SSD **není vhodné** pro dlouhodobé zálohování kvůli degradaci buněk při nečinnosti  
Zdroj: Backblaze (2023), CSIS (2022)

---

### 🔒 Bezpečnost záloh

- **Zálohy by měly být chráněny stejně jako produkční data**
  - Šifrování AES-256 (při přenosu i v klidu)
  - MFA pro přístup k cloudovým zálohám
  - Fyzická ochrana offline médií (trezor, sejf)

- **Testování obnovy** alespoň čtvrtletně (disaster recovery drill)

📌 Nepodléhej falešnému pocitu bezpečí – záloha je k ničemu, pokud nejde obnovit  
Zdroj: SANS Institute (2022)

---

### 🧰 Doporučené nástroje

| Nástroj       | Platforma |
|---------------|-----------|
| **Veeam**     | Windows, Linux, VMware |
| **Restic**    | Open source CLI, šifrování by default |
| **BorgBackup**| Deduplication, Linux-friendly |
| **Duplicati** | GUI, šifrování, pro domácí použití |
| **Timeshift** | Snapshoty systému (Linux) |
| **Rsync + Cron** | Vlastní skripty pro pokročilé |

---

### 🧭 ASCII diagram – Zálohovací topologie

```
    +-------------+
    |  Produkční  |
    |    server   |
    +------+------+
           |
        (Backup job)
           ↓
    +------+------+
    |  Lokální    |  <--- první kopie (např. NAS)
    |  záloha     |
    +------+------+
           |
        (Sync/Push)
           ↓
    +------+------+
    |  Off-site    |  <--- druhá kopie (cloud, offline disk, páska)
    |  záloha      |
    +-------------+
```

---

### 📚 Citace a zdroje (Harvard)

- Vacca, J.R. (2020). *Computer and Information Security Handbook*. 3rd ed. Elsevier.
- Veeam (2023). *What Is the 3-2-1 Backup Rule?* [online] Available at: https://www.veeam.com/blog/3-2-1-rule.html
- NIST (2021). *SP 800-209 – Security Guidelines for Storage Infrastructure*
- Backblaze (2023). *SSD vs HDD reliability*. Available at: https://www.backblaze.com/blog/how-long-do-ssds-last/
- SANS Institute (2022). *Backup and Restore Strategies*. https://www.sans.org/white-papers/backup-strategies/
