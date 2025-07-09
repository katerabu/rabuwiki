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

# Zkopíruj obrázky z markdown/obrazky do navody/obrazky
SRC_IMG_DIR = os.path.join(MARKDOWN_DIR, 'obrazky')
DST_IMG_DIR = os.path.join(HTML_DIR, 'obrazky')

if os.path.exists(SRC_IMG_DIR):
    shutil.rmtree(DST_IMG_DIR, ignore_errors=True)
    shutil.copytree(SRC_IMG_DIR, DST_IMG_DIR)
    print("🖼️ Složka s obrázky byla zkopírována do navody/obrazky/")

# Načti všechny .md soubory
files = [f for f in os.listdir(MARKDOWN_DIR) if f.endswith('.md')]

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
  <!-- GitHub Markdown CSS -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/github-markdown-css/5.2.0/github-markdown.min.css">
  <style>
    body {{
      max-width: 900px;
      margin: 2em auto;
      padding: 1em 2em;
      background-color: #fff;
    }}
    .markdown-body table {{
      border-collapse: collapse;
      width: 100%;
      margin-bottom: 1em;
    }}
    .markdown-body th,
    .markdown-body td {{
      border: 1px solid #d0d7de;
      padding: 6px 13px;
    }}
    .markdown-body th {{
      background-color: #f6f8fa;
      font-weight: 600;
      text-align: left;
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
  <ul>
''')
    for name, html_file in navody_html:
        f.write(f'    <li><a href="navody/{html_file}">{name}</a></li>\n')
    f.write('  </ul>\n</body>\n</html>')

# Automatické commitnutí a push
try:
    subprocess.run(['git', 'add', '.'], check=True)
    subprocess.run(['git', 'commit', '-m', 'Automatická aktualizace wiki'], check=True)
    subprocess.run(['git', 'push'], check=True)
    print("✅ Změny odeslány na GitHub.")
except subprocess.CalledProcessError as e:
    print("⚠️ Git commit/push selhal – možná nejsou žádné změny.")
