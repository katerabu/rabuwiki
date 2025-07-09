# Jak vytvořit osobní wiki na GitHub Pages

## 1. Předpoklady
- GitHub účet
- Git nainstalovaný (`git --version`)
- VS Code nebo jiný editor
- Python 3 (`python3 --version`)

## 2. Struktura wiki
Vytvoř složku např. `moje-wiki`, uvnitř budou:

- `markdown/` – Markdown soubory návodů
- `navody/` – generované HTML návody
- `index.html` – hlavní rozcestník s heslem
- `generate.py` – skript pro generování

## 3. Použití
Po přidání nového `.md` souboru spusť:


## 4. Upload na GitHub
```bash
git add .
git commit -m "Aktualizace wiki"
git push
