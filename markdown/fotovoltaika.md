---
title: Návratnost fotovoltaické elektrárny (FVE) s baterií – případ Kyjov, 2026
category: Domácnost
tags: [FVE, fotovoltaika, ekonomika, domácnost]
last_update: 2025-12-19
---

# Návratnost fotovoltaické elektrárny (FVE) s baterií – případ Kyjov, 2026

## 1. Popis systému

- **FVE výkon:** 4,95 kWp  
- **Baterie:** Solax T-BAT H 11,6 kWh (využitelná kapacita ~11 kWh, LiFePO4)  
- **Střídač:** Solax X3 Hybrid 10,0 kW  
- **Cena instalace:** 394 000 Kč (vč. DPH)  
- **Umístění:** Kyjov, Česká republika  
- **Spotřeba domácnosti 2026:** ~4 MWh, plánovaný nárůst na 5 MWh kvůli 2× TČ vzduch-vzduch  

Systém zahrnuje optimizéry na každý panel, možnost omezené zálohy (limited backup) a monitoring výroby.

---

## 2. Cenové vstupy – tarif MND D02 3x25 A

| Komponenta | Cena (Kč/MWh nebo Kč/měs) | Množství / měsíční platba |
|------------|---------------------------|--------------------------|
| Obchodní část – VT | 3 366,94 Kč/MWh | podle spotřeby |
| Distribuční část – VT | 2 171,45 Kč/MWh | podle spotřeby |
| Měsíční platba jistič | 235,00 Kč | měsíčně |
| Platba POZE | 495,00 Kč/MWh | podle spotřeby |
| Systémové služby ČEPS | 170,92 Kč/MWh | podle spotřeby |
| Měsíční paušál obchodní část | 99,17 Kč | měsíčně |

> Pozn.: všechny ceny bez DPH, použité pro výpočet ročních nákladů.

# Přehled klíčových komponent FVE + baterie – cena a procentuální podíl

| Část systému | Popis | Cena (Kč, vč. DPH) | Podíl na celkové investici (%) | Vizualizace podílu |
|-------------|-------|------------------|-------------------------------|------------------|
| **FV panely** | 11× 450 W bifaciální panely, konstrukce, montáž | 81 000 | 20,5 | ██████████ |
| **Střídač** | Solax X3 Hybrid 10 kW + elektroměr, wifi/LAN | 121 200 | 30,7 | ████████████████████ |
| **Baterie** | Solax T-BAT H 11,6 kWh (2× T58, LiFePO4) | 38 700 | 9,8 | ███████ |
| **Rozvaděč a elektromateriál** | DC + AC, zapojení backupu, montáž | 41 400 | 10,5 | ████████ |
| **Backup / ostrovní funkce** | Komponenty pro zálohu, limitovaný backup | 24 400 | 6,2 | ████ |
| **Elektromontážní práce** | Instalace všech komponent, revize, zprovoznění | 24 400 | 6,2 | ████ |
| **Elektroměrový rozvaděč + Cloud Connect / Tigo kit** | Monitoring, optimalizéry, přístupový bod | 24 000 | 6,1 | ████ |
| **Ostatní (bleskojistka, montážní materiál, drobné položky)** | Zprovoznění, revize, příslušenství | 12 400 | 3,1 | ██ |

**Celkem:** 367 500 Kč  

> Pozn.: Procentuální podíl je vztažen k celkové investici ~367 500 Kč (zaokrouhlené ceny). Celková fakturovaná cena nabídky je 394 000 Kč.

---

## 3. Roční výroba a spotřeba elektřiny – 2026

### 3.1. Měsíční profil výroby, spotřeby a nákladů FVE (kWh) 

| Měsíc      | Výroba FVE (kWh) | Spotřeba (kWh) | Spotřeba ze sítě (kWh) | Pokrytí (%) | Vizualizace pokrytí | Náklad na síť (Kč) |
|-----------|-----------------|----------------|------------------------|-------------|-------------------|------------------|
| Leden     | 99              | 573            | 474                    | 17          | ███░░░░░░░░░░░░░░░ | 2 940            |
| Únor      | 291             | 673            | 382                    | 43          | █████░░░░░░░░░░░░░ | 2 370            |
| Březen    | 497             | 553            | 56                     | 90          | █████████████░░░░░ | 348              |
| Duben     | 640             | 337            | 0                      | 100         | ████████████████████ | 0                |
| Květen    | 668             | 261            | 0                      | 100         | ████████████████████ | 0                |
| Červen    | 686             | 285            | 0                      | 100         | ████████████████████ | 0                |
| Červenec  | 672             | 302            | 0                      | 100         | ████████████████████ | 0                |
| Srpen     | 615             | 297            | 0                      | 100         | ████████████████████ | 0                |
| Září      | 478             | 217            | 0                      | 100         | ████████████████████ | 0                |
| Říjen     | 310             | 317            | 0                      | 100         | ████████████████████ | 0                |
| Listopad  | 105             | 277            | 172                    | 38          | █████░░░░░░░░░░░░░░░ | 1 067            |
| Prosinec  | 66              | 433            | 367                    | 15          | ███░░░░░░░░░░░░░░░░░ | 2 278            |

**Celkem výroba FVE 2026:** 5 874 kWh  
**Celková spotřeba 2026:** 4 000 kWh (původně 5 MWh se započítáním TČ)  
**Elektřina ze sítě:** 1 055 kWh  
**Celkový náklad na elektřinu ze sítě:** 6 545 Kč  

> Poznámka: Některé panely mohou být částečně zastíněny, snížení výroby cca 5–15 % nebylo zahrnuto.  

---

## 4. Roční úspory a návratnost

### 4.1. Úspory dle ceny elektřiny

Roční cena elektřiny bez FVE (bez DPH):

- **Obchodní část:** 4 000 kWh × 3 366,94 Kč/MWh = 13 468 Kč  
- **Distribuce + jistič:** 4 000 kWh × 2 171,45 Kč/MWh + 12×235 Kč = 10 886 + 2 820 = 13 706 Kč  
- **Platba POZE + systémové služby:** 4 000 kWh × (495 + 170,92) Kč/MWh = 2 664 Kč  

**Celkem náklady 2026 bez FVE:** ~29 838 Kč  

Roční náklady se zapojenou FVE:  
- Elektřina ze sítě: 1 055 kWh → náklad 6 545 Kč  
- Úspora = 29 838 – 6 545 ≈ 23 293 Kč  

---

### 4.2. Scénáře návratnosti podle dotace

| Dotace | Investice po dotaci (Kč) | Roční úspora (Kč) | Návratnost (let) |
|--------|---------------------------|-----------------|----------------|
| 0 %    | 394 000                   | 23 293          | 16,9           |
| 20 %   | 315 200                   | 23 293          | 13,5           |
| 30 %   | 275 800                   | 23 293          | 11,8           |
| 40 %   | 236 400                   | 23 293          | 10,1           |

> Pozn.: Úspory se mohou zvyšovat s růstem ceny elektřiny, čímž se návratnost zkracuje.

---

### 4.3. Dopad nárůstu spotřeby (TČ 5 MWh)

- Spotřeba 5 MWh ročně → ze sítě cca 2 000 kWh → úspora klesá na ~20 000 Kč/rok  
- Návratnost bez dotace: 394 000 / 20 000 ≈ 19,7 let  
- Návratnost s 30 % dotací: 275 800 / 20 000 ≈ 13,8 let  

---

## 5. Shrnutí

- Roční spotřeba: 4–5 MWh → s FVE a baterií pokryta z 80–95 %  
- Roční úspora: 20–23 tis. Kč (bez dotace)  
- Návratnost: 11–17 let dle dotace a spotřeby  
- Baterie: pokrytí víkendů, vyrovnání noční spotřeby  
- Backup: omezený, plný backup není nutný  

> Optimizéry řeší stínění panelů, střídač je předimenzovaný pro prevenci přehřívání, baterie zajišťuje víkendovou soběstačnost.

---

## 6. Doporučení

- Monitorovat výrobu a stav baterie  
- Pravidelná kontrola střídače a rozvaděče  
- Plánovat spotřebiče při omezené záloze  
- Zohlednit případný nárůst spotřeby (TČ, elektromobil)  

---

## 7. Zdroje

1. [MND – Tarif D02](https://www.mnd.cz)  
2. [Solax X3 Hybrid datasheet](https://www.solaxpower.com)  
3. [Solax T-BAT H 11,6 LiFePO4](https://www.solaxpower.com/battery)  
4. [ČEPS – systémové služby](https://www.ceps.cz)  
5. Solární profil ČR – [Český hydrometeorologický ústav, 2024]  
6. Podpora POZE – [Energetický regulační úřad](https://www.eru.cz)  
