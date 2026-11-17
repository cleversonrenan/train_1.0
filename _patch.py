# -*- coding: utf-8 -*-
# v0.5 — obras: ponte 2, tunel 3, com limite de obras no jogo

p = "REGRAS_v0.4.md"
s = open(p, encoding="utf-8").read()

# --- §1b: rio e serra passam a ser obras
old3 = """- **Rio** (coluna central): atravessar custa **3** (ponte). Ele **não bloqueia**, mas cobra pedágio
  em cada hexágono de água.
- **Serra** (leste e cunha central): custa 3. A cunha central fecha o meio do mapa."""
new3 = """- **Rio** (coluna central): atravessar exige **ponte** (2 mil). Ele **não bloqueia**,
  mas cada hexágono de água é uma obra.
- **Serra** (leste e cunha central): atravessar exige **túnel** (3 mil). A cunha central
  fecha o meio do mapa."""
assert old3 in s, "1b nao encontrado"
s = s.replace(old3, new3)

# --- §3: tabela de custos + limite de obras
old = """**Custos de construção** (por hexágono atravessado, em milhares):

| Terreno | Custo |
|---|---|
| Planície | 1 |
| Água (rio) | 2 |
| Montanha | 3 |
| Cruzar cume (borda grossa) | +2 |

Dinheiro é anotado no painel. Não existe dinheiro físico."""

new = """**Custos de construção** (por hexágono atravessado, em milhares):

| O que você constrói | Custo |
|---|---|
| Leito comum (planície) | 1 |
| **PONTE** (sobre água) | 2 |
| **TÚNEL** (pela montanha) | 3 |

**Obras são limitadas.** Você tem **2 pontes e 2 túneis** para o jogo inteiro — marque o
quadradinho no painel quando usar.

Essa é a regra que faz o mapa doer. Sem bloqueio entre jogadores (cada um desenha na
própria folha), o que cria disputa é a **escassez de travessia**: existem poucos lugares
baratos para cruzar o rio e a serra, e quem planeja a rede em volta deles chega primeiro.
O Vau do Corvo é a única travessia que **não gasta obra nenhuma**.

Dinheiro é anotado no painel. Não existe dinheiro físico."""
assert old in s, "tabela de custos nao encontrada"
s = s.replace(old, new)
s = s.replace("regras v0.4", "regras v0.5")
open("REGRAS_v0.5.md", "w", encoding="utf-8", newline="\n").write(s)

# --- folha
p = "gerar_folha.py"
g = open(p, encoding="utf-8").read()
o = '''txt(PX, 161, "CUSTO POR HEXÁGONO", size=3.2, anchor="start", weight="bold")
txt(PX, 166.5, "planície 1  ·  água 3 (rio)  ·  montanha 3  ·  cume +2", size=2.5, anchor="start")
txt(PX, 171, "no Vau do Corvo o rio custa 1", size=2.5, anchor="start", fill="#666")'''
n = '''txt(PX, 160, "CUSTO POR HEXÁGONO", size=3.2, anchor="start", weight="bold")
txt(PX, 165.5, "leito 1  ·  ponte 2  ·  túnel 3", size=2.6, anchor="start")
txt(PX, 170.2, "OBRAS NO JOGO:  2 pontes, 2 túneis", size=2.5, anchor="start", weight="bold")
for i in range(2):
    add(f'<rect x="{PX + 52 + i * 6:.1f}" y="167.0" width="4" height="4" fill="none" stroke="#111" stroke-width="0.45"/>')
    add(f'<rect x="{PX + 70 + i * 6:.1f}" y="167.0" width="4" height="4" fill="none" stroke="#111" stroke-width="0.45"/>')
txt(PX, 174.8, "Vau do Corvo: travessia livre, sem obra", size=2.5, anchor="start", fill="#666")'''
assert o in g, "bloco de custo nao encontrado"
g = g.replace(o, n)

o2 = '''txt(PX, 176, "GARFO: gaste 2 formas do kit.", size=2.8, anchor="start", weight="bold")
txt(PX, 180.5, "O trilho entra por 1 portal e sai por 2.", size=2.5, anchor="start", fill="#555")
txt(PX, 187, "Trilho cruza a borda sempre em ângulo reto,", size=2.5, anchor="start", fill="#555")
txt(PX, 191.5, "dentro do portal. A curva é feita no miolo do hex.", size=2.5, anchor="start", fill="#555")'''
n2 = '''txt(PX, 181.5, "GARFO: gaste 2 formas do kit.", size=2.8, anchor="start", weight="bold")
txt(PX, 186, "O trilho entra por 1 portal e sai por 2.", size=2.5, anchor="start", fill="#555")
txt(PX, 192, "O trilho cruza a borda em ângulo reto, dentro do portal.", size=2.5, anchor="start", fill="#555")
txt(PX, 196.5, "A curva é feita no miolo do hexágono.", size=2.5, anchor="start", fill="#555")'''
assert o2 in g, "bloco garfo nao encontrado"
g = g.replace(o2, n2).replace("v0.4", "v0.5")
open(p, "w", encoding="utf-8", newline="\n").write(g)
print("ok")
