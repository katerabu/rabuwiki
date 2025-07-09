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
