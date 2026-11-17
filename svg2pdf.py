# -*- coding: utf-8 -*-
"""Converte a folha do jogador (SVG, A4 paisagem) em PDF, via Chrome headless.
Gera duas versoes: 1:1 (borda a borda) e com margem de seguranca para impressora."""
import subprocess
import sys
import tempfile
from pathlib import Path

CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
SVG = "folha_jogador_v0.5.svg"

JOBS = [
    (1.00, "Folha_do_Jogador_v0.5.pdf"),
    (0.94, "Folha_do_Jogador_v0.5_margem_segura.pdf"),
]

HTML = """<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">
<title>{titulo}</title>
<style>
  @page {{ size: 297mm 210mm; margin: 0; }}
  html, body {{ margin: 0; padding: 0; width: 297mm; height: 210mm;
    display: flex; align-items: center; justify-content: center; overflow: hidden; }}
  svg {{ display: block; width: {w}mm; height: {h}mm; }}
</style></head><body>
{svg}
</body></html>"""


def build(scale: float, pdf_file: str) -> None:
    svg = Path(SVG).read_text(encoding="utf-8")
    doc = HTML.format(
        titulo=Path(pdf_file).stem,
        svg=svg,
        w=round(297 * scale, 2),
        h=round(210 * scale, 2),
    )
    tmp = Path(tempfile.gettempdir()) / (Path(pdf_file).stem + ".html")
    tmp.write_text(doc, encoding="utf-8")

    out = Path(pdf_file).resolve()
    cmd = [
        CHROME,
        "--headless=new",
        "--disable-gpu",
        "--no-pdf-header-footer",
        "--virtual-time-budget=4000",
        f"--print-to-pdf={out}",
        tmp.as_uri(),
    ]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if not out.exists():
        print(r.stdout, r.stderr)
        sys.exit("falhou: " + pdf_file)
    print("ok:", out.name, round(out.stat().st_size / 1024, 1), "KB")


for escala, nome in JOBS:
    build(escala, nome)
