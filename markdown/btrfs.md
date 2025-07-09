```markdown
# 🧱 Btrfs – moderní souborový systém

Btrfs (B-tree File System) je moderní souborový systém pro Linux, navržený jako náhrada za ext4, ZFS a další. Je zaměřen na spolehlivost, škálovatelnost a pokročilé funkce.

---

## 🕰️ Krátká historie

- Vývoj zahájen 2007 (Chris Mason, původně Oracle)
- Hlavní cíle:
  - snapshots (snímky)
  - checksumming (ochrana dat)
  - komprese
  - vestavěný RAID
  - copy-on-write (COW)
- Od jádra Linuxu 2.6.29 (2009) dostupný v mainline kernelu
- Dnes stabilní a podporovaný ve většině distribucí (např. openSUSE, Fedora, Ubuntu, Debian)

---

## 🧩 Klíčové vlastnosti

| Funkce                | Popis |
|-----------------------|-------|
| **Copy-on-Write (CoW)** | Nová data jsou zapsána vedle starých – šetří disk a zvyšuje bezpečnost |
| **Snapshots**          | Rychlé a efektivní zálohování celých stavů FS |
| **Subvolume**          | Oddělené oddíly uvnitř jednoho Btrfs FS |
| **Transparentní komprese** | Podpora Zlib, Zstd, LZO |
| **Checksumming**       | Detekce a oprava chyb na úrovni dat i metadata |
| **Vestavěný RAID**     | RAID 0/1/10/5/6 bez potřeby externího softwaru |
| **Send/Receive**       | Efektivní přenos snapshotů mezi systémy |

---

## 🔧 Použití v Linuxu – základní příkazy

### 📁 Vytvoření Btrfs souborového systému

```bash
sudo mkfs.btrfs /dev/sdX
```

### 🔍 Zjištění info o souborovém systému

```bash
sudo btrfs filesystem show
sudo btrfs filesystem df /mnt
```

### 📦 Připojení se subvolume

```bash
sudo mount -o subvol=@ /dev/sdX /mnt
```

### 📸 Snapshoty

```bash
sudo btrfs subvolume snapshot /mnt/@ /mnt/@_snapshot_nazev
```

### 🧹 Mazání snapshotu

```bash
sudo btrfs subvolume delete /mnt/@_snapshot_nazev
```

### 💾 Send/Receive (zálohování)

```bash
sudo btrfs send /mnt/@_snapshot_nazev | gzip > snapshot.gz
```

---

## 🧪 Testování a lab

```bash
sudo mkfs.btrfs /dev/loop0
sudo mount /dev/loop0 /mnt/test
sudo btrfs subvolume create /mnt/test/@home
sudo btrfs subvolume snapshot /mnt/test/@home /mnt/test/@home_snapshot
```

---

## ⚠️ Na co si dát pozor

- RAID5/6 stále **experimentální** – používat s opatrností
- Fragmentace u velkých zápisů – sledovat pomocí:
  ```bash
  sudo btrfs filesystem defragment -r /mnt
  ```
- Snapshoty nesmažou původní data – pozor na místo na disku

---

## 💻 Btrfs ve Windows

Btrfs není oficiálně podporovaný ve Windows, ale existují způsoby:

### 🛠️ WinBtrfs

- Otevřený ovladač pro Windows:
  🔗 https://github.com/maharmstone/btrfs
- Umožňuje čtení i zápis Btrfs disků
- Podpora subvolumes a RAID

### 🔒 Přístup přes WSL2

- Není přímá podpora Btrfs
- Možnosti:
  - Mount přes `WinBtrfs`
  - Nebo přístup přes sdílený disk z Linux VM

---

## 📌 Kde se Btrfs používá

- **openSUSE** – výchozí FS
- **Fedora** – od verze 33 výchozí
- **Ubuntu** – dostupný, ale není výchozí
- Vhodný pro:
  - NAS servery
  - Snapshot/zálohování desktopů
  - Virtuální prostředí

---

## 📚 Odkazy

- [Oficiální wiki Btrfs](https://btrfs.readthedocs.io/en/latest/)
- [ArchWiki – Comparison of file systems](https://wiki.archlinux.org/title/Comparison_of_file_systems)
- [Btrfs man pages](https://man7.org/linux/man-pages/man8/btrfs.8.html)
- [WinBtrfs projekt na GitHubu](https://github.com/maharmstone/btrfs)
```
