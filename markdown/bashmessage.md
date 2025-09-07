---
title: BashMessage – odesílání zpráv z příkazové řádky linuxu
category: Počítače
tags: [linux, echo, tcpdump, bash, message]
last_update: 2025-09-07
---
# Odesílání a příjem zprávy pomocí `ncat` a `nc` s `tcpdump` 🚀

Tento návod ukazuje, jak používat **`tcpdump`** pro naslouchání a logování UDP paketů a jak odesílat zprávy pomocí **`ncat`** nebo **`nc`**. Vše s přidaným logováním do souboru pro snadnou kontrolu zpráv. 📂

## Co budete potřebovat 🛠️

1. **Ubuntu** (nebo jiné Linux distro, ale pro tento příklad předpokládáme Ubuntu 🐧).
2. **`tcpdump`** pro naslouchání a logování paketů.
3. **`ncat`** (součást balíku **Nmap**) pro odesílání zpráv přes UDP 📡.
4. **`nc`** pro odesílání zpráv (alternativa k `ncat`) 💬.
5. Oprávnění pro spuštění **`tcpdump`** (obvykle jako root nebo pomocí `sudo`).

### Instalace potřebných nástrojů (pro Ubuntu) 📦

Nejdříve je třeba nainstalovat **`tcpdump`**, **`nmap`** (pro `ncat`), a **`netcat`** (pro `nc`).

Spusťte následující příkazy:

sudo apt update  
sudo apt install tcpdump nmap netcat  

Tímto získáte všechny potřebné nástroje. ✅

## 1. Naslouchání s `tcpdump` 🔍

Na počítači, který bude přijímat zprávy, použijte následující příkaz pro naslouchání na specifikovaném UDP portu a IP adrese.

### Příkaz pro naslouchání na UDP portu a IP:

sudo tcpdump -i eth0 -v -A udp and host 10.20.1.4 and port 4444

### Vysvětlení parametrů:
- `-i eth0` – Určuje síťové rozhraní, na kterém **`tcpdump`** bude poslouchat. Na Ubuntu může být toto rozhraní různé, např. `enp3s0`, `wlan0` nebo jiný název. Zkontrolujte svůj název síťového rozhraní příkazem `ip a`.
- `-v` – Verbózní režim pro zobrazení podrobností o každém zachyceném paketu.
- `-A` – Zobrazuje obsah paketů v textovém (ASCII) formátu.
- `udp` – Filtruje pouze UDP pakety.
- `and host 10.20.1.4` – Filtruje provoz pouze z nebo na specifikovanou IP adresu (v tomto případě `10.20.1.4`).
- `and port 4444` – Filtruje provoz pouze na UDP portu **4444**.

## 2. Odesílání zprávy (varianta 1: pomocí `ncat`) 📨

Tato varianta používá **`ncat`** k odeslání zprávy přes UDP protokol na specifikovaný port a IP adresu.

### Příkaz pro odeslání zprávy:

echo -n "Ahoj, toto je testovací zpráva!" | ncat -vu 10.20.1.4 4444

### Vysvětlení parametrů:
- `echo -n "Ahoj, toto je testovací zpráva!"` – Odesílá zprávu (s parametrem `-n` pro vynechání nového řádku na konci).
- `ncat -vu` – Používá **`ncat`** pro odeslání zprávy. `-v` pro verbózní výstup a `-u` pro UDP komunikaci.
- `10.20.1.4` – IP adresa cílového počítače.
- `4444` – UDP port, na který se zpráva odesílá.

## 3. Odesílání zprávy (varianta 2: pomocí `nc`) 💬

Tato varianta používá **`nc`** pro odesílání zprávy na specifikovanou IP adresu a port. Pokud nemáte **`ncat`**, můžete použít **`nc`**, který je často předinstalován v systémech.

### Příkaz pro odeslání zprávy:

echo -n "Ahoj, toto je testovací zpráva!" | nc -vu 10.20.1.4 4444

### Vysvětlení parametrů:
- `echo -n "Ahoj, toto je testovací zpráva!"` – Odesílá zprávu.
- `nc -vu` – Používá **`nc`** pro odesílání zprávy. `-v` pro verbózní výstup a `-u` pro UDP komunikaci.
- `10.20.1.4` – IP adresa cílového počítače.
- `4444` – UDP port, na který se zpráva odesílá.

## 4. Logování UDP zpráv do souboru 📜

Pro snadné logování přijatých zpráv použijeme **`tcpdump`** s přesměrováním výstupu do souboru. Tento soubor pak můžete použít pro kontrolu zpráv.

### Příkaz pro logování zpráv do souboru:

sudo tcpdump -vAi eth0 host 10.20.1.4 and port 4444 >> $HOME/messagesncat.log

### Vysvětlení parametrů:
- `-vA` – Verbózní režim pro podrobnosti o paketech a ASCII výstup pro textovou podobu dat.
- `-i eth0` – Síťové rozhraní pro naslouchání (nahraďte `eth0` podle potřeby).
- `>> $HOME/messagesncat.log` – Přesměruje výstup **`tcpdump`** do souboru `messagesncat.log` ve vašem domovském adresáři. **`>>`** znamená, že nové zprávy budou **přidány** k již existujícímu obsahu souboru. Pokud chcete soubor přepsat, použijte **`>`** (např. `> $HOME/messagesncat.log`).

### Zobrazení logovaných zpráv:

Pokud chcete zobrazit obsah logu, použijte příkaz:

cat $HOME/messagesncat.log

**Důležité rozdíly mezi `>` a `>>`:**
- **`>`** přepíše obsah souboru (záznamy budou ztraceny).
- **`>>`** přidá nové záznamy na konec souboru, aniž by přepsal jeho obsah.

## 5. Výstup z `tcpdump` 🎯

Pokud vše probíhá správně, **`tcpdump`** na serveru (počítá se, že server naslouchá na IP `10.20.1.4` a portu 4444) zachytí tento UDP paket a zobrazí výstup podobný tomuto:

10:10:10.123456 IP (tos 0x0, ttl 64, id 12345, offset 0, flags [none], proto UDP (17), length 60)  
    10.20.1.4.4444 > 10.20.1.10.12345: [bad udp cksum 0x1234 -> 0x4321!] UDP, length 32  
        0x0000:  4500 003c 3039 4000 4011 0000 0a14 01f4  
        0x0010:  0a14 01f6 01bb 1155 0016 89ab 6162 6364  
        0x0020:  6869 2c20 746f 746f 2069 7320 7465 7374  
        0x0030:  696e 6720 7a70 7261 7661 2100  

### Vysvětlení výstupu:
- **`10:10:10.123456`** – Časový razítko, kdy paket přišel.
- **`IP 10.20.1.4.4444 > 10.20.1.10.12345`** – Zobrazuje zdrojovou a cílovou IP adresu a porty.
- **`length 60`** – Délka dat v paketu.
- **Data (hexadecimální formát)** – Hexadecimální reprezentace datového obsahu paketu.
