---
title: Btrfs – moderní souborový systém pokračování
category: Počítače
tags: [linux, souborový systém, btrfs, snapshoty, raid]
last_update: 2025-07-09
---

# 📸 Snapshot a rollback – návod

✅ **Předpoklady:**  
- Máš systém nebo data na Btrfs subvolume (např. `/` nebo `/home`).  
- Snapshoty se vytvářejí z read-write subvolume.  
- Jsi v Linuxu s oprávněním root.

---

## 📍 Zjištění subvolumes

```bash
sudo btrfs subvolume list /
```

Například u openSUSE nebo Ubuntu s Btrfs jako root můžeš vidět:

```
ID 256 gen 128 top level 5 path @
ID 257 gen 129 top level 5 path @home
```

- Subvolume `@` = root (`/`)  
- Subvolume `@home` = domovské adresáře (`/home`)

---

## 📸 Vytvoření snapshotu

```bash
sudo btrfs subvolume snapshot /@ /mnt/btrfs_snapshots/@_preupdate
```

Tím vytvoříš snapshot aktuálního stavu rootu (`/`) do složky `/mnt/btrfs_snapshots`.  
Složku musíš mít vytvořenou!

---

## 🔁 Rollback (obnovení snapshotu)

Rollback rootu většinou děláš při bootu z Live USB nebo z jiného systému – protože nemůžeš mazat aktivní root.

### **Postup:**

1. Nabootuj z Live USB (např. Ubuntu)
2. Připoj Btrfs oddíl:

```bash
sudo mount /dev/sdXn /mnt
```

3. Smaž aktuální subvolume `@`:

```bash
sudo btrfs subvolume delete /mnt/@
```

4. Obnov snapshot jako nový `@`:

```bash
sudo btrfs subvolume snapshot /mnt/btrfs_snapshots/@_preupdate /mnt/@
```

5. Odpoj a restartuj.

---

# 🔍 Scrub – kontrola integrity

Scrub prohledá všechny bloky a ověří kontrolní součty.  
Pokud máš redundanci (např. RAID1), může Btrfs automaticky opravit chyby.

---

## 🔎 Spuštění scrubu

```bash
sudo btrfs scrub start /mountpoint
```

Např.:

```bash
sudo btrfs scrub start /
```

Proces běží na pozadí.

---

## 📋 Stav scrubu

```bash
sudo btrfs scrub status /
```

**Příklad výstupu:**

```
scrub status for UUID ...
    scrub started at Tue Jul  9 16:20:01 2025 and finished after 00:02:34
    total bytes scrubbed: 15.23GiB with 0 errors
```

---

## 🛑 Zastavení scrubu (pokud je potřeba)

```bash
sudo btrfs scrub cancel /
```

---

## ✅ Tipy

- Scrub můžeš automatizovat pomocí `cron` nebo `systemd` timeru (doporučeno 1× měsíčně).
- Snapshoty můžeš uchovávat i na jiném subvolumu/disku a přenášet pomocí `btrfs send/receive`.
