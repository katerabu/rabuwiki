---
title: rsync – zálohování v linuxu
category: Počítače
tags: [linux, zalohovani]
last_update: 2025-07-09
---

## začneme příklady:

## příklad 1 uložit zde: /etc/cron.hourly/rsync-bocxod 

# zalohovani z rpi5 na bocxod
# nezalohuje spatne pojmenovane soubory
# spousti se v "crontab -e" bez sudo! 
# "-a" zachovají se všechny atributy souborů, jako jsou oprávnění, časy a vlastníci.
# "-v" zobrazí informace o průběhu zálohování.
# "-z" komprimuje přenos dat, což může urychlit přenos, pokud zálohujete na vzdálené zařízení. 
# "--delete" soubory a adresáře, které byly odstraněny ze zdrojového adresáře, budou také odstraněny z cílového umístění.
# "-r" včetně vnořených podadresářů
# bez delete
echo "===============" >> /var/log/rsync-bocxod
date >> /var/log/rsync-bocxod
rsync -avr --omit-dir-times -e ssh liko@10.20.1.5:/home/liko/Share/ /home/liko/Backup/ 
echo "synchronizace Share rpi5 -> Backup bocxod dokoncena..." >> /var/log/rsync-bocxod
# echo "VYPNUTO - zakonmentovano v /etc/cron.hourly/rsync-bocxod" >> /var/log/rsync-bocxod 

## příklad 2 s delete uložit zde: /etc/cron.daily/rsync-bocxod-delete 

# zalohovani z rpi5 na bocxod
# nezalohuje spatne pojmenovane soubory
# spousti se v "crontab -e" bez sudo! 
# "-a" zachovají se všechny atributy souborů, jako jsou oprávnění, časy a vlastníci.
# "-v" zobrazí informace o průběhu zálohování.
# "-z" komprimuje přenos dat, což může urychlit přenos, pokud zálohujete na vzdálené zařízení. 
# "--delete" soubory a adresáře, které byly odstraněny ze zdrojového adresáře, budou také odstraněny z cílového umístění.
# "-r" včetně vnořených podadresářů
echo "===============" >> /var/log/rsync-bocxod
date >> /var/log/rsync-bocxod
rsync -avr --omit-dir-times --delete -e ssh liko@10.20.1.5:/home/liko/Share/ /home/liko/Backup/
echo "soubory smazane na Share rpi5 -> smazany taktez z Backup bocxod..." >> /var/log/rsync-bocxod
echo "synchronizace Share rpi5 -> Backup bocxod dokoncena..." >> /var/log/rsync-bocxod
# echo "VYPNUTO - zakonmentovano v /etc/cron.hourly/rsync-bocxod" >> /var/log/rsync-bocxod 

# 🔁 `rsync` – efektivní synchronizace souborů

`rsync` je mocný nástroj pro synchronizaci souborů a adresářů mezi dvěma místy – lokálně i přes síť. Umí přenášet pouze změny, zachovávat oprávnění a je ideální pro zálohování.

---

## 📦 Základní syntaxe

```bash
rsync [volby] zdroj cíl
```

Například:

```bash
rsync -av /home/user/ /mnt/backup/home/
```

- `-a` – archivní mód (zachová symlinky, oprávnění, časy, atd.)
- `-v` – verbose (výstupní informace)

> 🔹 Uvozovka **/ na konci zdrojového adresáře** znamená "obsah adresáře", bez lomítka by kopíroval i samotný adresář.

---

## 📁 Praktické příklady

### 1. 📥 Lokální kopie dat

```bash
rsync -av /data/ /backup/data/
```

Synchronizuje obsah `/data/` do `/backup/data/`.

### 2. 🌐 Kopie přes SSH

```bash
rsync -av -e ssh /home/user/ user@remote:/backup/user/
```

Přenese soubory přes SSH na vzdálený server.

### 3. 🔄 Z obou stran synchronizovat změny (pomocí `--update`)

```bash
rsync -avu /source/ /dest/
```

Volba `--update` zaručuje, že novější soubory nebudou přepsány staršími.

---

## 🧹 Mazání souborů, které už nejsou ve zdroji

```bash
rsync -av --delete /src/ /dst/
```

Smaže soubory v cíli, které už neexistují ve zdroji.

> ⚠️ Používej opatrně – můžeš přijít o data.

---

## 📑 Vyloučení souborů

```bash
rsync -av --exclude '*.tmp' /src/ /dst/
```

Ignoruje všechny soubory s příponou `.tmp`.

---

## 🔍 Suchý běh (co by rsync udělal)

```bash
rsync -av --dry-run /src/ /dst/
```

Nevykoná akci, jen vypíše, co by se stalo.

---

## 💡 Užitečné přepínače

| Přepínač       | Popis                                              |
|----------------|-----------------------------------------------------|
| `-a`           | Archivní mód (rekurze, symlinky, časy, oprávnění…)  |
| `-v`           | Verbose – výpis akcí                                |
| `--delete`     | Smazat soubory v cíli, které nejsou ve zdroji       |
| `--exclude`    | Vynechat soubory podle vzoru                        |
| `--progress`   | Zobrazit průběh kopírování                          |
| `--dry-run`    | Zobrazit, co by se stalo, ale neprovádět změny      |
| `-e ssh`       | Přenos přes SSH                                     |
| `--update`     | Nepřepisuj novější soubory                          |

---

## 🧪 Testovací příklad

```bash
rsync -av --dry-run --delete /home/user/ /mnt/backup/home/
```

Simuluje synchronizaci `/home/user/` do zálohy na `/mnt/backup/home/`, včetně mazání souborů, které již ve zdroji nejsou.

---

## 🛡️ Tipy pro bezpečné použití

- Nejprve si vždy vyzkoušej příkaz s `--dry-run`
- Dbej na správné lomítko na konci cest (`/`)
- Před použitím `--delete` zálohuj cílová data
- Vytvářej skripty pro pravidelnou zálohu s logováním

---

## 📚 Další odkazy

- [Oficiální man page rsync](https://man7.org/linux/man-pages/man1/rsync.1.html)
- [rsync na ArchWiki](https://wiki.archlinux.org/title/rsync)
- [rsync examples](https://linuxize.com/post/how-to-use-rsync-for-local-and-remote-data-transfer-and-synchronization/)
