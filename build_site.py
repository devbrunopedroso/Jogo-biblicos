#!/usr/bin/env python3
"""Monta a pasta site/ para publicar na Vercel.

Os jogos e a apresentação são escritos sem <html>/<head> (formato de Artifact).
Este script copia cada um para site/, acrescenta o cabeçalho HTML completo
e um botão para voltar à página inicial.

Uso:  python3 build_site.py      (rode de novo sempre que editar um jogo)
"""
from pathlib import Path

ROOT = Path(__file__).parent
SITE = ROOT / "site"

# arquivo de origem -> nome publicado no site
PAGES = {
    "antivirus-de-paulo.html": "apresentacao.html",
    "hacker-do-pensamento.html": "hacker-do-pensamento.html",
    "defesa-da-mente.html": "defesa-da-mente.html",
    "trilha-do-firewall.html": "trilha-do-firewall.html",
}

HEAD = """<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<style>body{margin:0}img{max-width:100%}[hidden]{display:none!important}
:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}
.home-link{position:fixed;left:12px;bottom:calc(12px + env(safe-area-inset-bottom,0px));z-index:50;
  font:400 20px 'VT323',ui-monospace,Menlo,monospace;color:#F4F1FF;background:rgba(17,15,54,.9);
  border:2px solid #3B358F;border-radius:10px;padding:4px 12px;text-decoration:none;opacity:.55}
.home-link:hover,.home-link:focus-visible{opacity:1;border-color:#5EC8FF}</style>
</head>
<body>
"""
FOOT = """
<a class="home-link" href="index.html" aria-label="Voltar para a página inicial">⌂ Início</a>
</body>
</html>
"""


def main():
    SITE.mkdir(exist_ok=True)
    for src, dst in PAGES.items():
        body = (ROOT / src).read_text(encoding="utf-8")
        (SITE / dst).write_text(HEAD + body + FOOT, encoding="utf-8")
        print(f"ok  {src} -> site/{dst}")
    print("Pronto. Publique a pasta site/ na Vercel.")


if __name__ == "__main__":
    main()
