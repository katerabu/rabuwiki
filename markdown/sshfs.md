---
title: sshfs – vzdaleny soubor pristup
category: Počítače
tags: [linux, samba, vzdaleneslozky]
last_update: 2025-07-09
---


# Návod na použití SSHFS pro Ubuntu a Windows 11

SSHFS (SSH File System) umožňuje připojit vzdálený souborový systém přes SSH jako by byl lokální. Tento návod popisuje, jak jej nastavit a používat na Ubuntu a Windows 11.

---

## Obsah
- [Co je SSHFS](#co-je-sshfs)
- [Použití na Ubuntu](#použití-na-ubuntu)
- [Použití na Windows 11](#použití-na-windows-11)
- [Užitečné příkazy](#užitečné-příkazy)
- [Zdroje](#zdroje)

---

## Co je SSHFS

SSHFS využívá protokol SSH pro připojení vzdáleného souborového systému jako lokálního. Na Linuxu využívá FUSE, na Windows je dostupný přes nástroje třetích stran.

---

## Použití na Ubuntu

### 1. Instalace SSHFS

sudo apt update
sudo apt install sshfs

### 2. Vytvoření mount pointu

mkdir ~/remote_mount

### 3. Připojení vzdáleného systému

sshfs username@remote_host:/cesta/k/adresari ~/remote_mount

### 4. Odpojení vzdáleného systému

fusermount -u ~/remote_mount
---

## Použití na Windows 11

Windows nativně SSHFS nepodporuje, použijeme nástroje třetích stran.

### Instalace WinFsp a SSHFS-Win

1. Stáhněte a nainstalujte [WinFsp](https://winfsp.dev/).
2. Stáhněte a nainstalujte [SSHFS-Win](https://github.com/billziss-gh/sshfs-win/releases).

### Připojení přes PowerShell

net use X: \sshfs\username@remote_host[\path]

Příklad:

net use X: \sshfs\john@192.168.1.100\home\john\documents

### Odpojení jednotky

net use X: /delete

---

## Užitečné příkazy

| Akce                 | Ubuntu                        | Windows (PowerShell)                      |
|----------------------|------------------------------|------------------------------------------|
| Připojit vzdálený FS | `sshfs user@host:/path ~/mnt`| `net use X: \\sshfs\user@host\path`     |
| Odpojit FS           | `fusermount -u ~/mnt`         | `net use X: /delete`                      |

---

## Zdroje

- Garfinkel, S., 2023. *SSHFS User Guide*. Dostupné z: https://github.com/libfuse/sshfs [cit. 2025-07-09].
- Ziss-gh, B., 2023. *SSHFS-Win: SSH File System for Windows*. Dostupné z: https://github.com/billziss-gh/sshfs-win [cit. 2025-07-09].
- Microsoft, 2024. *Mount Network Drive using net use*. Dostupné z: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/net-use [cit. 2025-07-09].

---

*Vytvořeno ChatGPT, 2025*

Původní návod již nedostupný, z https://wiki.ubuntu.cz/sshfs upravený zde: 

# Připojení vzdáleného souborového systému pomocí **SSHFS** 🔒🗂️

**SSH** je bezpečnostní protokol, který se používá pro bezpečnou komunikaci mezi počítači. **SSHFS** je nástroj, který umožňuje připojení vzdáleného souborového systému k místnímu počítači pomocí SSH. Tento nástroj je ideální pro práci s distantními adresáři a soubory, jelikož:
- **Bezpečné připojení**: SSH autentizuje připojení a šifruje komunikaci, takže vaše data jsou chráněna.
- **Jednoduché použití**: S SSHFS se můžete snadno připojit k vzdálenému adresáři bez složité konfigurace.
- **Transparentní připojení**: Systém se chová, jako by byl adresář místní, takže můžete pracovat s těmito soubory stejně jako s lokálními.

## Co budete potřebovat 🔧

1. **Ubuntu** (nebo jiné Linux distro).
2. **SSH server** spuštěný na vzdáleném počítači (předpokládáme, že už máte SSH přístup k vzdálenému stroji).
3. **Práva pro instalaci a přidání uživatele do fuse skupiny**.

---

## Instalace SSHFS na Ubuntu 📦

Nejdříve nainstalujte balíček **`sshfs`**. Otevřete terminál a spusťte následující příkaz:

sudo apt-get update  
sudo apt-get install sshfs

### Přidání uživatele do fuse skupiny 👥

Pro použití SSHFS musíte být členem **fuse** skupiny, aby bylo možné využívat **fusermount**. Tuto změnu je nutné provést, jinak se vám při pokusu o použití SSHFS zobrazí chybová hláška o oprávněních.

Pro přidání uživatele do skupiny **fuse** použijte tento příkaz:

sudo adduser $USER fuse

Po přidání uživatele do skupiny se musíte **odhlásit** a **znovu přihlásit**, aby se změny projevily. 🔄

---

## Použití SSHFS pro připojení vzdáleného adresáře 📂

Nyní, když máte SSHFS nainstalováno a vaše uživatelská práva jsou správně nastavena, můžete připojit vzdálený adresář. Předpokládejme, že chcete připojit vzdálený adresář **/projekty** z počítače **vzdaleny**. Tento adresář připojíte k místnímu adresáři **~/projekty**.

### Příkaz pro připojení vzdáleného adresáře:

sshfs $USER@vzdaleny:/projekty ~/projekty

- **$USER** – Vaše uživatelské jméno na vzdáleném počítači.
- **vzdaleny** – Název nebo IP adresa vzdáleného počítače.
- **/projekty** – Cesta k adresáři na vzdáleném počítači.
- **~/projekty** – Místní adresář, kam bude vzdálený adresář připojen.

---

## Odpojení vzdáleného adresáře 🚪

Pokud chcete odpojit vzdálený adresář, použijte následující příkaz:

fusermount -u ~/projekty

Tento příkaz odpojí vzdálený adresář a vrátí vás zpět na místní souborový systém.

---

## Automatické připojení při startu pomocí /etc/fstab 📑

Pro automatické připojení vzdáleného adresáře při každém startu počítače můžete přidat záznam do souboru **/etc/fstab**. Příkaz vypadá takto:

### Přidání do `/etc/fstab`:

sshfs#franta@vzdaleny:/projekty /home/franta/projekty fuse defaults 0 0

- **franta** – Změňte na své uživatelské jméno.
- **vzdaleny** – IP adresa nebo název vzdáleného počítače.
- **/projekty** – Cesta k adresáři na vzdáleném počítači.
- **/home/franta/projekty** – Místní adresář pro připojení.

Tento zápis zajišťuje, že při každém startu systému se vzdálený adresář automaticky připojí.

---

## Pozor na UID (Uživatelské identifikační číslo) ⚠️

U jednoho uživatele v systému může být UID odlišné na místním a vzdáleném počítači. **UID** je unikátní číslo přidělené každému uživatelskému účtu v systému, a může se lišit mezi počítači.

Pokud máte například na místním počítači UID 1000 a na vzdáleném 1003, při použití příkazu **`ls -l`** uvidíte na vzdáleném systému jiný uživatelský název, ale to není problém. **SSHFS** stále používá správné UID na vzdáleném počítači, takže všechny změny budou provedeny správně, bez ohledu na to, jaký uživatelský název je zobrazen.

Pokud chcete vidět UID, použijte příkaz:

ls -l

---

## Závěr ✨

SSHFS je skvělý nástroj pro bezpečné a jednoduché připojení vzdálených adresářů na Linuxových systémech. Využití SSH pro šifrování a autentizaci připojení znamená, že vaše data jsou chráněna a přenosy souborů jsou bezpečné.

Teď víte, jak nainstalovat, nastavit a používat SSHFS na vašem Ubuntu stroji. Pokud máte jakékoliv dotazy nebo problémy, neváhejte se zeptat! 😊




