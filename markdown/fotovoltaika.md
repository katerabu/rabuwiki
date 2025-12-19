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
| Leden     | 99              | 453            | 354                    | 22          | █░░░░░░░░░░░░░░░░░░ | 2 196            |
| Únor      | 291             | 503            | 212                    | 58          | ██████░░░░░░░░░░░░░ | 1 315            |
| Březen    | 497             | 443            | 0                      | 100         | ████████████████████ | 0                |
| Duben     | 640             | 307            | 0                      | 100         | ████████████████████ | 0                |
| Květen    | 668             | 241            | 0                      | 100         | ████████████████████ | 0                |
| Červen    | 686             | 270            | 0                      | 100         | ████████████████████ | 0                |
| Červenec  | 672             | 292            | 0                      | 100         | ████████████████████ | 0                |
| Srpen     | 615             | 287            | 0                      | 100         | ████████████████████ | 0                |
| Září      | 478             | 247            | 0                      | 100         | ████████████████████ | 0                |
| Říjen     | 310             | 297            | 0                      | 100         | ████████████████████ | 0                |
| Listopad  | 105             | 277            | 172                    | 38          | █████░░░░░░░░░░░░░░░ | 1 067            |
| Prosinec  | 66              | 383            | 317                    | 17          | ███░░░░░░░░░░░░░░░░░ | 1 967            |

**Celkem výroba FVE 2026:** 5 874 kWh  
**Celková spotřeba 2026:** 4 000 kWh  
**Elektřina ze sítě:** 1 055 kWh  
**Celkový náklad na elektřinu ze sítě:** 6 545 Kč
**Poznámka:** Ve skutečnosti mohou být některé panely částečně zastíněny (např. stín od komína, stromy, části střechy), což může snížit výrobu FVE v některých měsících o cca 5–15 %. 
Tento faktor nebyl v tabulce zohledněn, ale je vhodné s ním při plánování a predikci úspor počítat. 
Výroba FVE + baterie pokryje prakticky celou domácí spotřebu, s rezervou na víkendy.

---

## 4. Výpočet ročních úspor

Roční cena elektřiny bez FVE (bez DPH):

- **Obchodní část:** 4 000 kWh × 3 366,94 Kč/MWh = 13 468 Kč  
- **Distribuce + jistič:** 4 000 kWh × 2 171,45 Kč/MWh + 12×235 Kč = 10 886 + 2 820 = 13 706 Kč  
- **Platba POZE + systémové služby:** 4 000 kWh × (495 + 170,92) Kč/MWh = 4 000 × 665,92 / 1 000 = 2 664 Kč  

**Celkem náklady 2026 bez FVE:** ~29 838 Kč  

Roční náklady se zapojenou FVE:  
- Většinu spotřeby pokrývá FVE → úspora cca 95 % spotřeby (ztráty + baterie) → **úspora ~28 000 Kč/rok**  

---

## 5. Návratnost investice

- **Cena instalace:** 394 000 Kč  
- **Roční úspora:** ~28 000 Kč  
- **Dotace:** zatím není známa (pokud např. 30 % → 118 183 Kč → investice klesne na 275 762 Kč)  

### 5.1. Bez dotace

Návratnost = 394 000 / 28 000 ≈ 14,1 let

> Pozn.: nezahrnuto zvýšení ceny elektřiny ani inflace, přesto realistické.

---

## 6. Predikce vývoje cen elektřiny

- Historicky +5–10 % ročně v ČR (regulovaná část, obchodní část volatilní)  
- Při růstu 5 % ročně:
  - Úspora v roce 2027 → 28 000 × 1,05 ≈ 29 400 Kč  
  - Úspora v roce 2030 → 28 000 × 1,05^4 ≈ 33 600 Kč  

➡️ **Návratnost se zkracuje**, protože FVE kryje stále dražší elektřinu.

---

## 7. Shrnutí

- **Roční spotřeba:** ~4 MWh → s FVE a baterií pokryta z ~95 %  
- **Roční úspora:** ~28 000 Kč (bez dotace)  
- **Návratnost:** 14 let bez dotace, 10 let s 30 % dotací  
- **Výhody baterie:** pokrytí víkendů a vyrovnání nočního odběru  
- **Optimální omezený backup:** pokrývá kritické okruhy při výpadku sítě, full backup není nutný  

> Systém je dobře dimenzovaný, optimizéry pokryjí stínění, střídač je předimenzovaný, aby se předešlo přehřívání, a baterie zajistí soběstačnost během víkendů.

---

## 8. Doporučení

- Monitoring výroby a stavu baterie pro optimalizaci využití  
- Periodická kontrola střídače a rozvaděče  
- Připravit jednoduchý plán spotřebičů při omezené záloze 
