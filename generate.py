import os
import markdown
import subprocess
import shutil

# Nejprve stáhni změny z GitHubu
try:
    subprocess.run(['git', 'pull', 'origin', 'main'], check=True)
    print("✅ Aktualizace z GitHubu proběhla.")
except subprocess.CalledProcessError:
    print("⚠️ Nepodařilo se provést git pull. Zkontroluj konflikt nebo připojení.")

# Cesty
MARKDOWN_DIR = 'markdown'
HTML_DIR = 'navody'
INDEX_FILE = 'index.html'

# Vytvoř složku pro HTML, pokud neexistuje
os.makedirs(HTML_DIR, exist_ok=True)

# Načti všechny .md soubory
files = [f for f in os.listdir(MARKDOWN_DIR) if f.endswith('.md')]

import shutil

SRC_IMG_DIR = os.path.join(MARKDOWN_DIR, 'obrazky')
DST_IMG_DIR = os.path.join(HTML_DIR, 'obrazky')

if os.path.exists(SRC_IMG_DIR):
    shutil.rmtree(DST_IMG_DIR, ignore_errors=True)
    shutil.copytree(SRC_IMG_DIR, DST_IMG_DIR)
    print("🖼️ Složka s obrázky byla zkopírována do navody/obrazky/")

# Vygeneruj HTML soubory
navody_html = []
for md_file in files:
    with open(os.path.join(MARKDOWN_DIR, md_file), 'r', encoding='utf-8') as f:
        text = f.read()
    html_content = markdown.markdown(text, extensions=['fenced_code'])
    
    name = os.path.splitext(md_file)[0]
    html_file = f'{name}.html'
    with open(os.path.join(HTML_DIR, html_file), 'w', encoding='utf-8') as f:
        f.write(f'''<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>{name}</title>
  <!-- Přidáno GitHub Markdown CSS -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/github-markdown-css/5.2.0/github-markdown.min.css">
  <style>
    body {{
      max-width: 900px;
      margin: 2em auto;
      padding: 1em 2em;
      background-color: #fff;
    }}
  </style>
</head>
<body>
  <article class="markdown-body">
{html_content}
    <p><a href="../index.html">← Zpět</a></p>
  </article>
</body>
</html>''')
    navody_html.append((name, html_file))

# Zkopíruj složku s obrázky (pokud existuje)
OBRAZKY_ZDROJ = os.path.join(MARKDOWN_DIR, 'obrazky')
OBRAZKY_CIL = 'obrazky'

if os.path.exists(OBRAZKY_ZDROJ):
    shutil.rmtree(OBRAZKY_CIL, ignore_errors=True)
    shutil.copytree(OBRAZKY_ZDROJ, OBRAZKY_CIL)
    print("🖼️  Složka s obrázky byla zkopírována.")

# Vygeneruj index.html
with open(INDEX_FILE, 'w', encoding='utf-8') as f:
    f.write('''<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>RabuKate Wiki</title>
  <script>
    const heslo = prompt("Zadej heslo:");
    if (heslo !== "tajne123") {
      document.write("Přístup zamítnut.");
      throw new Error("Špatné heslo");
    }
  </script>
</head>
<body>
  <h1>RabuKate Wiki</h1>

  <table border="1" cellpadding="8" cellspacing="0">
    <thead>
      <tr>
        <th>Návod (HTML)</th>
        <th>Markdown (.md)</th>
      </tr>
    </thead>
    <tbody>
''')
    for name, html_file in navody_html:
        md_file = f'{name}.md'
        f.write(f'''      <tr>
        <td><a href="navody/{html_file}">{name}</a></td>
        <td><a href="markdown/{md_file}">{md_file}</a></td>
      </tr>
''')
    f.write('''    </tbody>
  </table>
</body>
</html>''')


import subprocess

# Automatické commitnutí a push
try:
    subprocess.run(['git', 'add', '.'], check=True)
    subprocess.run(['git', 'commit', '-m', 'Automatická aktualizace wiki'], check=True)
    subprocess.run(['git', 'push'], check=True)
    print("✅ Změny odeslány na GitHub.")
except subprocess.CalledProcessError as e:
    print("⚠️ Git commit/push selhal – možná nejsou žádné změny.")
