# -*- coding: utf-8 -*-
"""Comparativo das duas marcacoes de portao. A4 retrato, unidades = mm."""
import math

R = 22.0
HEXH = math.sqrt(3) * R
S = []

def add(s): S.append(s)

def txt(x, y, s, size=4.0, anchor="middle", weight="normal", fill="#111"):
    add(f'<text x="{x:.2f}" y="{y:.2f}" font-size="{size}" text-anchor="{anchor}" '
        f'font-family="Segoe UI, Arial, sans-serif" font-weight="{weight}" fill="{fill}">{s}</text>')

def vert(x, y, k):
    a = math.radians(60 * k)
    return x + R * math.cos(a), y - R * math.sin(a)

def gate(x, y, k):
    a = math.radians(30 + 60 * k)
    ap = R * math.sqrt(3) / 2
    return (x + ap * math.cos(a), y - ap * math.sin(a)), (math.cos(a), -math.sin(a))

def hexpath(x, y):
    pts = [vert(x, y, k) for k in range(6)]
    return "M " + " L ".join(f"{a:.2f},{b:.2f}" for a, b in pts) + " Z"

def edge(x, y, k):
    """retorna (p1, p2) da borda k"""
    return vert(x, y, k), vert(x, y, (k + 1) % 6)

def cluster(x0, y0, modo, n=3):
    """desenha n hexagonos em linha, com a marcacao do modo escolhido"""
    centros = []
    for c in range(n):
        x = x0 + R + 1.5 * R * c
        y = y0 + HEXH / 2 + (HEXH / 2 if c % 2 else 0)
        centros.append((x, y))
    for (x, y) in centros:
        add(f'<path d="{hexpath(x, y)}" fill="#fff" stroke="#333" stroke-width="0.35"/>')

    for (x, y) in centros:
        for k in range(6):
            (gx, gy), (nx, ny) = gate(x, y, k)
            tx, ty = -ny, nx              # tangente à borda
            if modo == "A":               # rasgo: duas marcas na direção da borda
                for s in (-1, 1):
                    cx, cy = gx + s * 3.4 * tx, gy + s * 3.4 * ty
                    add(f'<line x1="{cx-2.2*tx:.2f}" y1="{cy-2.2*ty:.2f}" '
                        f'x2="{cx+2.2*tx:.2f}" y2="{cy+2.2*ty:.2f}" '
                        f'stroke="#111" stroke-width="0.45" stroke-linecap="round"/>')
            else:                          # portal: trecho engrossado + dois batentes
                w = 2.0
                add(f'<line x1="{gx-w*tx:.2f}" y1="{gy-w*ty:.2f}" '
                    f'x2="{gx+w*tx:.2f}" y2="{gy+w*ty:.2f}" '
                    f'stroke="#111" stroke-width="1.3"/>')
                for s in (-1, 1):
                    cx, cy = gx + s * w * tx, gy + s * w * ty
                    add(f'<line x1="{cx-2.4*nx:.2f}" y1="{cy-2.4*ny:.2f}" '
                        f'x2="{cx+2.4*nx:.2f}" y2="{cy+2.4*ny:.2f}" '
                        f'stroke="#111" stroke-width="0.45" stroke-linecap="round"/>')
    return centros

def rail(pontos):
    d = "M " + " L ".join(f"{a:.2f},{b:.2f}" for a, b in pontos)
    add(f'<path d="{d}" fill="none" stroke="#b3261e" stroke-width="1.0" '
        f'stroke-linecap="round" stroke-linejoin="round"/>')

def exemplo(centros, modo):
    (x1, y1), (x2, y2) = centros[1], centros[2]
    # RETA no hexágono do meio: portão 2 -> portão 5
    g2, _ = gate(x1, y1, 2)
    g5, _ = gate(x1, y1, 5)
    rail([(g2[0] - 6, g2[1] - 5), (x1, y1), (g5[0] + 6, g5[1] + 5)])
    # GARFO no hexágono da direita: entra portão 2, sai 4 e 0
    ga, _ = gate(x2, y2, 2)
    gb, _ = gate(x2, y2, 4)
    gc, _ = gate(x2, y2, 0)
    rail([(ga[0] - 6, ga[1] - 5), (x2, y2)])
    rail([(x2, y2), (gb[0] + 5, gb[1] + 6)])
    rail([(x2, y2), (gc[0] + 5, gc[1] - 6)])

add('<svg xmlns="http://www.w3.org/2000/svg" width="210mm" height="297mm" viewBox="0 0 210 297">')
add('<rect width="100%" height="100%" fill="#fff"/>')

txt(105, 16, "QUAL MARCAÇÃO DE PORTÃO?", size=7, weight="bold")
txt(105, 21.5, "as duas funcionam igual; muda só o que o lápis vê", size=3.4, fill="#666")

txt(14, 36, "A — RASGO  (o que eu tinha desenhado)", size=4.6, anchor="start", weight="bold")
txt(14, 41, "duas marcas PARALELAS à borda. O trilho corre pelo rasgo entre elas.", size=3.2, anchor="start", fill="#555")
c1 = cluster(50, 48, "A")
exemplo(c1, "A")

txt(14, 158, "B — PORTAL  (o que você desenhou)", size=4.6, anchor="start", weight="bold")
txt(14, 163, "dois BATENTES perpendiculares + trecho engrossado. O trilho passa entre os batentes.", size=3.2, anchor="start", fill="#555")
c2 = cluster(50, 170, "B")
exemplo(c2, "B")

txt(105, 262, "no tamanho real de impressão (borda de 12 mm) os dois ficam assim:", size=3.2, fill="#555")

# amostra em tamanho real: R=12
def mini_hex(x, y, r, modo, rotulo):
    global R
    old = R
    R = r
    add(f'<path d="{hexpath(x, y)}" fill="#fff" stroke="#333" stroke-width="0.3"/>')
    for k in range(6):
        (gx, gy), (nx, ny) = gate(x, y, k)
        tx, ty = -ny, nx
        if modo == "A":
            for s in (-1, 1):
                cx, cy = gx + s * 2.4 * tx, gy + s * 2.4 * ty
                add(f'<line x1="{cx-1.5*tx:.2f}" y1="{cy-1.5*ty:.2f}" x2="{cx+1.5*tx:.2f}" '
                    f'y2="{cy+1.5*ty:.2f}" stroke="#111" stroke-width="0.35" stroke-linecap="round"/>')
        else:
            add(f'<line x1="{gx-1.5*tx:.2f}" y1="{gy-1.5*ty:.2f}" x2="{gx+1.5*tx:.2f}" '
                f'y2="{gy+1.5*ty:.2f}" stroke="#111" stroke-width="0.9"/>')
            for s in (-1, 1):
                cx, cy = gx + s * 1.5 * tx, gy + s * 1.5 * ty
                add(f'<line x1="{cx-2.0*nx:.2f}" y1="{cy-2.0*ny:.2f}" x2="{cx+2.0*nx:.2f}" '
                    f'y2="{cy+2.0*ny:.2f}" stroke="#111" stroke-width="0.35" stroke-linecap="round"/>')
    R = old
    txt(x, y + r + 6, rotulo, size=3.0)

mini_hex(55, 272, 12, "A", "A")
mini_hex(95, 272, 12, "B", "B")
mini_hex(135, 272, 12, "B  (batente maior)", "B+")

add('</svg>')
open("comparativo_marcacao.svg", "w", encoding="utf-8").write("\n".join(S))
print("ok", len(S))
