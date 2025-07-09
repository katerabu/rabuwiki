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
