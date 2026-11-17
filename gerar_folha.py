# -*- coding: utf-8 -*-
"""Folha do jogador — Bacia do Corvo v0.5
Marcacao B (portal): dois batentes perpendiculares + trecho engrossado na borda.
Unidades do SVG = milimetros."""

import math

R = 12.0
COLS, ROWS = 9, 6
MAP_X, MAP_Y = 6.0, 24.0
PAGE_W, PAGE_H = 297.0, 210.0
HEXH = math.sqrt(3) * R

# portal: proporcoes tiradas do desenho do autor, com piso de legibilidade
PORTAL_W = max(0.09 * R, 1.2)   # meio-comprimento ao longo da borda
CAP = max(0.065 * R, 1.4)       # meio-comprimento do batente (perpendicular)
BAR_SW = 0.9
CAP_SW = 0.42

MAPA = [row.split() for row in [
    ".  4  10 .  ~  .  .  11 ^",
    ".  1  .  .  ~  .  .  ^  ^",
    ".  .  .  .  ~  .  .  3  ^",
    ".  .  ^  ^  12 ^  ^  .  5",
    ".  6  .  .  ~  .  7  .  .",
    "~  .  .  8  ~  2  .  9  .",
]]

# nome, cor da cidade, cubos impressos, cinza
CIDADES = {
    1:  ("PORTO NORTE",  "A", ["P", "M"], False),
    2:  ("FOZ DO CORVO", "A", ["V", "X"], False),
    3:  ("PASSO ALTO",   "?", [],          True),
    4:  ("SERRA NEGRA",  "M", ["A", "V"], False),
    5:  ("ESTANCIA SUL", "V", ["P", "X"], False),
    6:  ("PONTE VELHA",  "X", ["A", "M"], False),
    7:  ("CURRAL",       "P", ["V", "M"], False),
    8:  ("BARRA FUNDA",  "V", ["P", "A"], False),
    9:  ("COSTA VERDE",  "X", ["M", "P"], False),
    10: ("VILA FERRO",   "P", ["A", "X"], False),
    11: ("BOCA DO MATO", "M", ["P", "V"], False),
    12: ("VAU DO CORVO", "?", [],          True),
}


def centro(c, r):
    x = MAP_X + R + 1.5 * R * c
    y = MAP_Y + HEXH / 2 + HEXH * r + (HEXH / 2 if c % 2 else 0)
    return x, y


def vertice(x, y, k, r=None):
    r = R if r is None else r
    a = math.radians(60 * k)
    return x + r * math.cos(a), y - r * math.sin(a)


def portao(x, y, k, r=None):
    r = R if r is None else r
    a = math.radians(30 + 60 * k)
    ap = r * math.sqrt(3) / 2
    nx, ny = math.cos(a), -math.sin(a)          # normal (para fora)
    return (x + ap * nx, y + ap * ny), (nx, ny)


def hexpath(x, y, r=None):
    pts = [vertice(x, y, k, r) for k in range(6)]
    return "M " + " L ".join(f"{a:.2f},{b:.2f}" for a, b in pts) + " Z"


S = []
def add(s): S.append(s)


def txt(x, y, s, size=3.0, anchor="middle", weight="normal", fill="#111"):
    add(f'<text x="{x:.2f}" y="{y:.2f}" font-size="{size}" text-anchor="{anchor}" '
        f'font-family="Segoe UI, Arial, sans-serif" font-weight="{weight}" fill="{fill}">{s}</text>')


def portal(x, y, k, r=None, sw_bar=BAR_SW, sw_cap=CAP_SW, w=None, cap=None):
    """marcacao B: batentes perpendiculares + trecho engrossado"""
    r = R if r is None else r
    w = (max(0.09 * r, 1.2) if w is None else w)
    cap = (max(0.065 * r, 1.4) if cap is None else cap)
    (gx, gy), (nx, ny) = portao(x, y, k, r)
    tx, ty = -ny, nx
    add(f'<line x1="{gx-w*tx:.2f}" y1="{gy-w*ty:.2f}" x2="{gx+w*tx:.2f}" y2="{gy+w*ty:.2f}" '
        f'stroke="#111" stroke-width="{sw_bar}"/>')
    for s in (-1, 1):
        cx, cy = gx + s * w * tx, gy + s * w * ty
        add(f'<line x1="{cx-cap*nx:.2f}" y1="{cy-cap*ny:.2f}" x2="{cx+cap*nx:.2f}" '
            f'y2="{cy+cap*ny:.2f}" stroke="#111" stroke-width="{sw_cap}" stroke-linecap="round"/>')


add(f'<svg xmlns="http://www.w3.org/2000/svg" width="{PAGE_W}mm" height="{PAGE_H}mm" '
    f'viewBox="0 0 {PAGE_W} {PAGE_H}">')
add('<rect width="100%" height="100%" fill="#fff"/>')

# ---------------- mapa
for r in range(ROWS):
    for c in range(COLS):
        cell = MAPA[r][c]
        x, y = centro(c, r)
        if cell == "~":
            add(f'<path d="{hexpath(x, y)}" fill="#dbe7ef" stroke="#333" stroke-width="0.3"/>')
            for dy in (-4.0, 0.0, 4.0):
                add(f'<path d="M {x-6.2:.1f},{y+dy:.1f} q 2,-1.3 3.1,0 q 1,1.3 3.1,0 q 2,-1.3 3.1,0" '
                    f'fill="none" stroke="#5b7f96" stroke-width="0.35"/>')
        elif cell == "^":
            add(f'<path d="{hexpath(x, y)}" fill="#e6e1d6" stroke="#333" stroke-width="0.3"/>')
            for ox in (-4.6, 0.4, 5.0):
                add(f'<path d="M {x+ox:.1f},{y+4.8:.1f} L {x+ox+2.6:.1f},{y-2.4:.1f} '
                    f'L {x+ox+5.2:.1f},{y+4.8:.1f} Z" fill="none" stroke="#6b5a45" stroke-width="0.4"/>')
        else:
            add(f'<path d="{hexpath(x, y)}" fill="#fff" stroke="#999" stroke-width="0.3"/>')

for r in range(ROWS):
    for c in range(COLS):
        x, y = centro(c, r)
        for k in range(6):
            portal(x, y, k)

# ---------------- cidades
for r in range(ROWS):
    for c in range(COLS):
        cell = MAPA[r][c]
        if not cell.isdigit():
            continue
        idx = int(cell)
        nome, cor, cubos, cinza = CIDADES[idx]
        x, y = centro(c, r)
        add(f'<path d="{hexpath(x, y)}" fill="{"#ececec" if cinza else "#faf7ef"}" '
            f'stroke="#111" stroke-width="1.0"/>')
        if cinza:
            add(f'<path d="{hexpath(x, y)}" fill="url(#hachura)" stroke="none"/>')
            txt(x, y - 2.0, "cinza", size=2.3, fill="#666")
            txt(x, y + 1.2, "urbanizar", size=2.3, fill="#666")
        else:
            add(f'<circle cx="{x:.2f}" cy="{y-6.0:.2f}" r="2.2" fill="none" stroke="#111" stroke-width="0.5"/>')
            txt(x, y - 5.1, cor, size=2.5, weight="bold")
            partes = nome.split()
            if len(partes) == 1:
                txt(x, y - 0.6, nome, size=2.8, weight="bold")
            else:
                txt(x, y - 1.9, partes[0], size=2.6, weight="bold")
                txt(x, y + 1.0, " ".join(partes[1:]), size=2.6, weight="bold")
            n = len(cubos)
            if n:
                passo = 4.3
                x0 = x - (n - 1) * passo / 2
                for i, cu in enumerate(cubos):
                    cx = x0 + i * passo
                    add(f'<rect x="{cx-1.85:.2f}" y="{y+4.2:.2f}" width="3.7" height="3.7" '
                        f'fill="#fff" stroke="#111" stroke-width="0.45"/>')
                    txt(cx, y + 7.15, cu, size=2.5, weight="bold")

# ---------------- painel
PX = 182.0
add(f'<line x1="{PX-3:.1f}" y1="8" x2="{PX-3:.1f}" y2="202" stroke="#ccc" stroke-width="0.3"/>')
txt(PX, 14, "BACIA DO CORVO", size=5.2, anchor="start", weight="bold")
txt(PX, 18.4, "folha do barão · v0.5", size=2.6, anchor="start", fill="#666")

txt(PX, 26, "MOTOR  (alcance da entrega)", size=3.2, anchor="start", weight="bold")
for i in range(5):
    x = PX + 10 * i
    add(f'<rect x="{x:.1f}" y="28.5" width="8.5" height="7" fill="none" stroke="#111" stroke-width="0.5"/>')
    txt(x + 4.25, 33.6, str(i + 1), size=3.6)

txt(PX, 42, "TRILHA DE RENDA", size=3.2, anchor="start", weight="bold")
rx0, rx1, ry = PX + 1, PX + 104, 49.0
add(f'<line x1="{rx0}" y1="{ry}" x2="{rx1}" y2="{ry}" stroke="#111" stroke-width="0.5"/>')
VALORES = {1: 3, 2: 4, 4: 6, 6: 8, 8: 10, 10: 12, 13: 14, 16: 16,
           20: 18, 24: 20, 28: 22, 32: 20, 36: 15, 40: 10}
for p in range(1, 41):
    x = rx0 + (rx1 - rx0) * (p - 1) / 39
    h = 2.6 if p in VALORES else 1.4
    add(f'<line x1="{x:.2f}" y1="{ry}" x2="{x:.2f}" y2="{ry-h:.2f}" stroke="#111" stroke-width="0.35"/>')
    if p in VALORES:
        txt(x, ry - 3.7, str(VALORES[p]), size=2.4)
        txt(x, ry + 3.0, str(p), size=2.0, fill="#777")

txt(PX, 59, "TÍTULOS   −1 PV cada · −1 mil por turno", size=3.0, anchor="start", weight="bold")
for i in range(10):
    x = PX + 3.7 * i
    add(f'<rect x="{x:.1f}" y="61.5" width="3.2" height="3.2" fill="none" stroke="#111" stroke-width="0.4"/>')

txt(PX, 72, "PRIMEIRA ENTREGA  (+3 cinza · +4 demais)", size=3.0, anchor="start", weight="bold")
for i, idx in enumerate(sorted(CIDADES)):
    nome, cor, cubos, cinza = CIDADES[idx]
    y = 77 + i * 4.3
    txt(PX, y, nome, size=2.5, anchor="start")
    txt(PX + 62, y, "+3" if cinza else "+4", size=2.5)
    add(f'<line x1="{PX+70}" y1="{y+0.7}" x2="{PX+95}" y2="{y+0.7}" stroke="#bbb" stroke-width="0.3"/>')

y0 = 129
txt(PX, y0, "SEU TURNO", size=3.2, anchor="start", weight="bold")
txt(PX, y0 + 4.6, "role 3d6  ·  rerrolar: 1 mil por dado", size=2.5, anchor="start", fill="#555")
txt(PX, y0 + 8.8, "3 ações, na ordem que quiser:", size=2.5, anchor="start", fill="#555")
for i, a in enumerate(["CONSTRUIR  1 peça = 1 forma do kit",
                       "ENTREGAR  até o alcance do motor",
                       "MELHORAR MOTOR  (8/12/16/20 mil)",
                       "URBANIZAR  10 mil"]):
    txt(PX, y0 + 13.4 + i * 4.4, "—  " + a, size=2.6, anchor="start")

txt(PX, 158.5, "CUSTO POR HEXÁGONO", size=3.2, anchor="start", weight="bold")
txt(PX, 163.5, "leito 1  ·  ponte 2  ·  túnel 3", size=2.6, anchor="start")

txt(PX, 168.5, "OBRAS NO JOGO", size=2.8, anchor="start", weight="bold")
for i, (rot, yy) in enumerate([("2 PONTES", 172.4), ("2 TÚNEIS", 176.6)]):
    txt(PX, yy, rot, size=2.5, anchor="start")
    for j in range(2):
        add(f'<rect x="{PX + 17 + j * 6:.1f}" y="{yy - 3.0:.1f}" width="4" height="4" '
            f'fill="none" stroke="#111" stroke-width="0.45"/>')

txt(PX, 181.0, "Vau do Corvo: travessia livre, sem obra", size=2.4, anchor="start", fill="#666")

txt(PX, 186, "GARFO: gaste 2 formas do kit.", size=2.8, anchor="start", weight="bold")
txt(PX, 190, "entra por 1 portal, sai por 2.", size=2.5, anchor="start", fill="#555")
txt(PX, 195, "O trilho cruza a borda em ângulo reto;", size=2.5, anchor="start", fill="#555")
txt(PX, 199, "a curva é feita no miolo do hexágono.", size=2.5, anchor="start", fill="#555")

# ---------------- legenda (rodapé)
LY = 172.0
add(f'<rect x="6" y="{LY-12}" width="168" height="36" fill="none" stroke="#ddd" stroke-width="0.3"/>')
txt(9, LY - 6.5, "AS TRÊS FORMAS — sempre de portal a portal", size=2.9, anchor="start", weight="bold")


def mini(cx, cy, entrada, saidas, rotulo, sub, r=7.2):
    add(f'<path d="{hexpath(cx, cy, r)}" fill="#fff" stroke="#999" stroke-width="0.3"/>')
    for k in range(6):
        portal(cx, cy, k, r=r, sw_bar=0.55, sw_cap=0.25, w=0.85, cap=1.0)
    def P(k):
        (gx, gy), _ = portao(cx, cy, k, r)
        return gx, gy
    for k in saidas:
        x1, y1 = P(entrada)
        x2, y2 = P(k)
        add(f'<path d="M {x1:.2f},{y1:.2f} L {cx:.2f},{cy:.2f} L {x2:.2f},{y2:.2f}" '
            f'fill="none" stroke="#b3261e" stroke-width="1.0" stroke-linejoin="round" stroke-linecap="round"/>')
    txt(cx, cy + 10.4, rotulo, size=2.9, weight="bold")
    txt(cx, cy + 13.6, sub, size=2.2, fill="#666")


mini(24, LY + 1, 1, [4], "RETA", "portal oposto")
mini(70, LY + 1, 1, [2], "CURVA 60°", "portal vizinho")
mini(116, LY + 1, 1, [3], "CURVA 120°", "salta um portal")
mini(156, LY + 1, 1, [0, 2], "GARFO", "1 entra · 2 saem")

add('<defs><pattern id="hachura" width="1.8" height="1.8" patternTransform="rotate(45)" '
    'patternUnits="userSpaceOnUse"><line x1="0" y1="0" x2="0" y2="1.8" stroke="#999" '
    'stroke-width="0.45"/></pattern></defs>')
add('</svg>')

with open("folha_jogador_v0.5.svg", "w", encoding="utf-8") as f:
    f.write("\n".join(S))
print("ok", len(S), "elementos")

