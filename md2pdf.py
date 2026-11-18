# -*- coding: utf-8 -*-
"""Converte as regras em Markdown num PDF A4, usando Chrome headless."""
import html
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

MD = "REGRAS_v0.5.md"
PDF_NAME = "Regras_Bacia_do_Corvo_v0.5.pdf"

CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"


def inline(t: str) -> str:
    t = html.escape(t)
    t = re.sub(r"`([^`]+)`", r"<code>\1</code>", t)
    t = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<em>\1</em>", t)
    return t


def parse(md: str) -> str:
    out, i = [], 0
    lines = md.split("\n")
    while i < len(lines):
        ln = lines[i]

        if not ln.strip():
            i += 1
            continue

        if ln.startswith("```"):
            buf = []
            i += 1
            while i < len(lines) and not lines[i].startswith("```"):
                buf.append(html.escape(lines[i]))
                i += 1
            i += 1
            out.append("<pre>" + "\n".join(buf) + "</pre>")
            continue

        if re.fullmatch(r"-{3,}", ln.strip()):
            out.append("<hr/>")
            i += 1
            continue

        m = re.match(r"^(#{1,4})\s+(.*)$", ln)
        if m:
            n = len(m.group(1))
            out.append(f"<h{n}>{inline(m.group(2))}</h{n}>")
            i += 1
            continue

        # tabela
        if ln.strip().startswith("|") and i + 1 < len(lines) and re.match(
            r"^\s*\|[\s:|-]+\|\s*$", lines[i + 1]
        ):
            head = [c.strip() for c in ln.strip().strip("|").split("|")]
            i += 2
            rows = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                rows.append([c.strip() for c in lines[i].strip().strip("|").split("|")])
                i += 1
            t = ["<table><thead><tr>"]
            t += [f"<th>{inline(c)}</th>" for c in head]
            t.append("</tr></thead><tbody>")
            for row in rows:
                t.append("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in row) + "</tr>")
            t.append("</tbody></table>")
            out.append("".join(t))
            continue

        if ln.startswith(">"):
            buf = []
            while i < len(lines) and lines[i].startswith(">"):
                buf.append(inline(lines[i].lstrip(">").strip()))
                i += 1
            out.append("<blockquote><p>" + "<br/>".join(buf) + "</p></blockquote>")
            continue

        if re.match(r"^\s*(\d+)\.\s+", ln):
            buf = []
            while i < len(lines) and re.match(r"^\s*(\d+)\.\s+", lines[i]):
                item = re.sub(r"^\s*\d+\.\s+", "", lines[i])
                i += 1
                while i < len(lines) and lines[i].startswith("   ") and lines[i].strip():
                    item += " " + lines[i].strip()
                    i += 1
                buf.append(f"<li>{inline(item)}</li>")
            out.append("<ol>" + "".join(buf) + "</ol>")
            continue

        if re.match(r"^\s*-\s+", ln):
            buf = []
            while i < len(lines) and re.match(r"^\s*-\s+", lines[i]):
                item = re.sub(r"^\s*-\s+", "", lines[i])
                i += 1
                while i < len(lines) and lines[i].startswith("  ") and lines[i].strip():
                    item += " " + lines[i].strip()
                    i += 1
                buf.append(f"<li>{inline(item)}</li>")
            out.append("<ul>" + "".join(buf) + "</ul>")
            continue

        buf = []
        while i < len(lines) and lines[i].strip() and not re.match(
            r"^(#{1,4}\s|-{3,}$|\||>\s*|\s*-\s|\s*\d+\.\s)", lines[i]
        ):
            buf.append(inline(lines[i].strip()))
            i += 1
        out.append("<p>" + "<br/>".join(buf) + "</p>")
    return "\n".join(out)


CSS = """
@page { size: A4; margin: 15mm 15mm 14mm 15mm; }
* { box-sizing: border-box; }
body { font-family: "Segoe UI", Arial, sans-serif; font-size: 9.7pt; line-height: 1.38;
       color: #14181d; margin: 0; }
h1 { font-size: 20pt; margin: 0 0 2mm 0; letter-spacing: -0.02em; }
h2 { font-size: 12.6pt; margin: 5mm 0 1.6mm 0; padding-bottom: 1mm;
     border-bottom: 0.5pt solid #d5d5d5; page-break-after: avoid; }
h3 { font-size: 10.8pt; margin: 3.8mm 0 1.2mm 0; page-break-after: avoid; }
p { margin: 0 0 1.9mm 0; }
ul, ol { margin: 0 0 2.2mm 0; padding-left: 6mm; }
li { margin-bottom: 0.8mm; }
table { border-collapse: collapse; width: 100%; margin: 2mm 0 4mm 0;
        font-size: 9.6pt; page-break-inside: avoid; break-before: avoid-page; }
th, td { border: 0.5pt solid #b9bec4; padding: 1.6mm 2.4mm; text-align: left;
         vertical-align: top; }
th { background: #eef1f4; font-weight: 600; }
td:nth-child(2), th:nth-child(2) { white-space: nowrap; }
hr { border: none; border-top: 0.5pt solid #dcdcdc; margin: 3.2mm 0; }
blockquote { margin: 1.8mm 0; padding: 1.6mm 3.5mm; background: #f4f6f8;
             border-left: 2.2pt solid #4a6b8a; }
blockquote p { margin: 0; }
code { font-family: Consolas, monospace; font-size: 9.4pt; background: #f0f2f4;
       padding: 0.3mm 1mm; border-radius: 1mm; }
pre { background: #f0f2f4; padding: 3mm; font-size: 9pt; overflow: hidden; }
strong { font-weight: 650; }
.cover { border-bottom: 1.6pt solid #14181d; padding-bottom: 3mm; margin-bottom: 6mm; }
.cover .sub { font-size: 9.6pt; color: #5a6470; margin-top: 1.5mm; }
"""


def main():
    md = Path(MD).read_text(encoding="utf-8")
    body = parse(md)

    # capa: tira o h1 do corpo e usa no cabeçalho
    m = re.match(r"<h1>(.*?)</h1>\s*", body)
    titulo = m.group(1) if m else "Regras"
    if m:
        body = body[m.end():]

    doc = f"""<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">
<title>{titulo}</title><style>{CSS}</style></head><body>
<div class="cover">
  <h1>{titulo}</h1>
  <div class="sub">Um jogo de lápis e dados para 1–2 barões · impresso em 1 folha por jogador</div>
</div>
{body}
</body></html>"""

    html_path = Path(tempfile.gettempdir()) / "regras_corvo.html"
    html_path.write_text(doc, encoding="utf-8")
    pdf_path = Path(PDF_NAME).resolve()

    cmd = [
        CHROME,
        "--headless=new",
        "--disable-gpu",
        "--no-pdf-header-footer",
        "--virtual-time-budget=4000",
        f"--print-to-pdf={pdf_path}",
        html_path.as_uri(),
    ]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if not pdf_path.exists():
        print(r.stdout, r.stderr)
        sys.exit("PDF nao gerado")
    print("ok:", pdf_path, round(pdf_path.stat().st_size / 1024, 1), "KB")


if __name__ == "__main__":
    main()
