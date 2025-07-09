import os
import markdown
import subprocess
import shutil

# --- Git pull ---
try:
    subprocess.run(['git', 'pull', 'origin', 'main'], check=True)
    print("✅ Aktualizace z GitHubu proběhla.")
except subprocess.CalledProcessError:
    print("⚠️ Nepodařilo se provést git pull. Zkontroluj konflikt nebo připojení.")

MARKDOWN_DIR = 'markdown'
HTML_DIR = 'navody'
INDEX_FILE = 'index.html'

os.makedirs(HTML_DIR, exist_ok=True)

# Kopíruj obrázky
SRC_IMG_DIR = os.path.join(MARKDOWN_DIR, 'obrazky')
DST_IMG_DIR = os.path.join(HTML_DIR, 'obrazky')

if os.path.exists(SRC_IMG_DIR):
    shutil.rmtree(DST_IMG_DIR, ignore_errors=True)
    shutil.copytree(SRC_IMG_DIR, DST_IMG_DIR)
    print("🖼️ Obrázky zkopírovány.")

# Získat seznam .md souborů
files = [f for f in os.listdir(MARKDOWN_DIR) if f.endswith('.md')]

# Pomocná funkce na získání data poslední změny z git logu
def get_git_last_modified_date(filepath):
    try:
        output = subprocess.check_output(
            ['git', 'log', '-1', '--format=%cd', '--', filepath],
            encoding='utf-8').strip()
        return output
    except subprocess.CalledProcessError:
        return "Neznámé"

navody_html = []
for md_file in files:
    md_path = os.path.join(MARKDOWN_DIR, md_file)
    with open(md_path, 'r', encoding='utf-8') as f:
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
    .markdown-body th, .markdown-body td {{
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
    last_modified = get_git_last_modified_date(md_path)
    navody_html.append((name, html_file, last_modified))

# Generování index.html s vyhledáváním, responsivním designem, menu, datem a login formulářem
with open(INDEX_FILE, 'w', encoding='utf-8') as f:
    f.write('''<!DOCTYPE html>
<html lang="cs">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>RabuKate Wiki</title>
  <style>
    body {
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji";
      margin: 0; padding: 0; background: #f7f9fc;
    }
    header {
      background: #0366d6; color: white; padding: 1em 1.5em;
      display: flex; align-items: center; justify-content: space-between;
      flex-wrap: wrap;
    }
    header h1 {
      margin: 0; font-size: 1.5em;
    }
    nav a {
      color: white; text-decoration: none; margin-left: 1em;
      font-weight: 600;
    }
    nav a:hover {
      text-decoration: underline;
    }
    main {
      max-width: 960px;
      margin: 2em auto;
      padding: 0 1em;
      background: white;
      border-radius: 6px;
      box-shadow: 0 2px 8px rgb(0 0 0 / 0.1);
    }
    #searchInput {
      width: 100%;
      max-width: 400px;
      padding: 8px 12px;
      margin-bottom: 1em;
      font-size: 1em;
      border: 1px solid #ccc;
      border-radius: 4px;
    }
    table {
      border-collapse: collapse;
      width: 100%;
    }
    th, td {
      text-align: left;
      padding: 10px 15px;
      border-bottom: 1px solid #ddd;
    }
    th {
      background-color: #f0f0f0;
    }
    tr:hover {
      background-color: #f5faff;
    }
    @media (max-width: 600px) {
      table, thead, tbody, th, td, tr {
        display: block;
      }
      thead tr {
        display: none;
      }
      tr {
        margin-bottom: 1em;
        border: 1px solid #ccc;
        border-radius: 6px;
        padding: 0.5em;
      }
      td {
        border: none;
        padding-left: 50%;
        position: relative;
      }
      td:before {
        position: absolute;
        top: 0.6em;
        left: 1em;
        width: 45%;
        white-space: nowrap;
        font-weight: 600;
      }
      td:nth-of-type(1):before { content: "Návod HTML"; }
      td:nth-of-type(2):before { content: "Návod GitHub (Markdown)"; }
      td:nth-of-type(3):before { content: "Poslední úprava"; }
    }
    /* Login form */
    #loginForm {
      max-width: 300px;
      margin: 2em auto;
      padding: 1em;
      background: #fff;
      border-radius: 6px;
      box-shadow: 0 2px 8px rgb(0 0 0 / 0.1);
      display: none;
    }
    #loginForm input[type="password"] {
      width: 100%;
      padding: 8px 12px;
      margin-bottom: 1em;
      border: 1px solid #ccc;
      border-radius: 4px;
      font-size: 1em;
    }
    #loginForm button {
      background: #0366d6;
      border: none;
      color: white;
      padding: 10px 16px;
      cursor: pointer;
      border-radius: 4px;
      font-size: 1em;
      width: 100%;
    }
    #loginError {
      color: red;
      margin-bottom: 1em;
      display: none;
    }
  </style>
</head>
<body>
  <header>
    <h1>RabuKate Wiki</h1>
    <nav>
      <a href="#">Domů</a>
      <a href="#">Kategorie 1</a>
      <a href="#">Kategorie 2</a>
    </nav>
  </header>
  <main id="mainContent" style="display:none;">
    <input type="text" id="searchInput" placeholder="Vyhledat návod...">
    <table id="navodyTable">
      <thead>
        <tr>
          <th>Návod HTML</th>
          <th>Návod GitHub (Markdown)</th>
          <th>Poslední úprava</th>
        </tr>
      </thead>
      <tbody>
''')

    for name, html_file, last_mod in navody_html:
        md_url = f"https://katerabu.github.io/rabuwiki/markdown/{name}.html"
        f.write(f'''        <tr>
          <td><a href="navody/{html_file}">{name}</a></td>
          <td><a href="{md_url}">{name}</a></td>
          <td>{last_mod}</td>
        </tr>
''')

    f.write('''      </tbody>
    </table>
  </main>

  <form id="loginForm">
    <div id="loginError">Špatné heslo, zkuste to znovu.</div>
    <input type="password" id="password" placeholder="Zadejte heslo">
    <button type="submit">Přihlásit se</button>
  </form>

  <script>
    const correctPassword = "tajne123";

    const loginForm = document.getElementById('loginForm');
    const mainContent = document.getElementById('mainContent');
    const loginError = document.getElementById('loginError');

    loginForm.style.display = "block";
    mainContent.style.display = "none";

    loginForm.addEventListener('submit', function(e) {
      e.preventDefault();
      const entered = document.getElementById('password').value;
      if (entered === correctPassword) {
        loginForm.style.display = "none";
        mainContent.style.display = "block";
        loginError.style.display = "none";
      } else {
        loginError.style.display = "block";
      }
    });

    // Vyhledávání v tabulce
    document.getElementById('searchInput').addEventListener('input', function() {
      const filter = this.value.toLowerCase();
      const rows = document.querySelectorAll('#navodyTable tbody tr');
      rows.forEach(row => {
        const text = row.textContent.toLowerCase();
        row.style.display = text.includes(filter) ? '' : 'none';
      });
    });
  </script>
</body>
</html>''')

# --- Automatický git commit a push ---
try:
    subprocess.run(['git', 'add', '.'], check=True)
    subprocess.run(['git', 'commit', '-m', 'Automatická aktualizace wiki'], check=True)
    subprocess.run(['git', 'push'], check=True)
    print("✅ Změny odeslány na GitHub.")
except subprocess.CalledProcessError as e:
    print("⚠️ Git commit/push selhal – možná nejsou žádné změny.")
