# Bacia do Corvo — regras v0.3

Jogo de tabuleiro de papel e lápis para 1–2 barões. 1 folha por jogador.
Impresso em 1 ou 2 folhas A4. Componentes: lápis, 3 dados de 6 faces, esta folha.

---

## 1. A GEOMETRIA (o coração)

Cada hexágono tem **6 portais**, um em cada borda. O portal é a **marcação dupla**:
dois **batentes perpendiculares** atravessando a borda, com um trecho engrossado entre eles.

O trilho é desenhado **entre os dois batentes**, sempre **em ângulo reto com a borda**.
Nunca se cruza uma borda fora de um portal. A curva é feita **no miolo do hexágono**,
não na borda.

Como a borda é compartilhada, o portal de um hexágono é o mesmo do vizinho:
o trilho encaixa sozinho, sem régua.

Existem só **três formas** de peça:

| Peça | Desenho | Uso de portais |
|---|---|---|
| **RETA** | portal → portal **oposto** | entra 1, sai 1 |
| **CURVA 60°** | portal → portal **vizinho** (lado a lado) | entra 1, sai 1 |
| **CURVA 120°** | portal → portal **saltando um** | entra 1, sai 1 |
| **GARFO** | portal → **dois** portais | entra 1, sai 2 |

**Um hexágono nunca recebe mais de uma peça.** Um portal pode ser usado por **duas peças
diferentes**, uma de cada lado — nunca duas do mesmo lado.

O garfo é a única peça que faz a rede ramificar. Ele é **caro** (ver §3).

## 1b. O MAPA — Bacia do Corvo

**9 × 6 hexágonos.** Uma bacia cercada de serra, cortada por um rio de norte a sul.

- **Rio** (coluna central): atravessar custa **3** (ponte). Ele **não bloqueia**, mas cobra pedágio
  em cada hexágono de água.
- **Serra** (leste e cunha central): custa 3. A cunha central fecha o meio do mapa.
- **O VAU DO CORVO** — único hexágono de **planície no meio da linha do rio**, encravado
  entre serra de um lado e água do outro. É o gargalo: passar por ali custa **1** em vez de 3.
  E é **cidade cinza**: quem urbanizar o Vau ganha um centro de carga no meio do mapa.
- **12 cidades**: 2 de cada cor (azul, preto, amarelo, vermelho, roxo) + 2 cinzas
  (Passo Alto, no leste, e o Vau). Cada cidade colorida traz **2 cubos impressos**.

---

## 2. O TURNO

Cada jogador **rola os seus próprios 3d6** no começo do seu turno e usa **apenas os
próprios resultados**. O resultado é o **kit do turno** dele.

Ninguém depende da sorte do vizinho: o seu turno é problema seu.

Cada face vale uma forma:

| d6 | Forma liberada |
|---|---|
| 1–2 | RETA |
| 3–4 | CURVA 60° |
| 5 | CURVA 120° |
| 6 | **LIVRE** (reta ou qualquer curva) |

Ex.: `3, 3, 6` → duas curvas de 60° e uma peça livre.

**Rerrolada (regra proposta, testar):** uma vez por turno, você pode rerrolar
**qualquer número** dos três dados. Vale o segundo resultado. É o seguro contra o
turno morto (três curvas de 120° que não servem para nada).

**A ordem de jogar agora importa pouco** (cada um tem a própria sorte), então não há leilão.
O marcador de primeiro jogador só serve para desempatar quem chega junto num bônus.

**No seu turno:**

1. Rola 3d6 (e pode rerrolar uma vez).
2. Faz **3 ações**, na ordem que quiser.
3. Recebe renda, paga dividendos, apaga as conexões incompletas.
4. Passa os dados ao próximo.

Ações possíveis:

- **CONSTRUIR** — desenha **1 peça**, gastando **1 forma** do kit.
  A peça tem de continuar a sua rede (ou começar num portal de cidade).
- **ENTREGAR** — ver §4.
- **MELHORAR MOTOR** — sobe 1 nível, paga o custo da tabela.
- **URBANIZAR** — 10 mil: converte 1 cidade cinza em cidade colorida e repõe cubos.

**Conexão incompleta** = peça desenhada sem chegar a uma cidade ou sem continuar a rede.
É **apagada no fim do turno**. Você perdeu o dinheiro.

---

## 3. O GARFO E O DINHEIRO

O **GARFO** não sai de uma face isolada. Ele é comprado:

> **Gaste 2 formas do kit** (quaisquer, inclusive iguais) **e pague o terreno** do hexágono.
> O garfo ocupa o hexágono inteiro e faz o trilho dividir em dois.

Assim o garfo é decisão, não sorte: com 3 formas no kit, abrir um garfo é
**entregar o turno inteiro** para ganhar duas frentes. É a jogada que ganha jogo.

**Custos de construção** (por hexágono atravessado, em milhares):

| Terreno | Custo |
|---|---|
| Planície | 1 |
| Água (rio) | 2 |
| Montanha | 3 |
| Cruzar cume (borda grossa) | +2 |

Dinheiro é anotado no painel. Não existe dinheiro físico.

---

## 4. ENTREGA (é aqui que se ganha)

Cada cidade imprime **cubos de cor** (1 a 3). Um cubo só pode ser entregue numa
**cidade da mesma cor** (cinza não recebe nada até ser urbanizada).

Na ação ENTREGAR:

1. Escolha 1 cubo impresso numa cidade.
2. Trace pela **sua** rede um caminho até uma cidade da cor do cubo.
3. O caminho pode ter no máximo **nível do motor** hexágonos.
4. Renda sobe = **nº de hexágonos do caminho**. Risque o cubo.

Se aquele era o **último cubo** da cidade, ela fica **abandonada**: risque o nome.
Isso aproxima o fim do jogo.

**Bônus de primeira entrega:** a primeira entrega feita em cada cidade dá
**+3** (cidades pequenas) ou **+4** (cidades grandes) na trilha de renda.
Só o primeiro; escreva suas iniciais no espaço. *(É a tradução direta das cartas
de círculo verde do Railways.)*

---

## 5. RENDA, TÍTULOS, FIM

**Trilha de renda** (0–40). A renda sobe com entregas e cai no fim:

| Posição | 1 | 2 | 4 | 6 | 8 | 10 | 13 | 16 | 20 | 24 | 28 | 32 | 36 | 40 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Recebe | 3 | 4 | 6 | 8 | 10 | 12 | 14 | 16 | 18 | 20 | 22 | 20 | 15 | 10 |

*(a curva invertida do Railways: o fim apodrece quem parou.)*

**Título:** a qualquer momento, +5 mil e **−1 PV no fim**, e **−1 mil de dividendo
por turno**. Sem dinheiro para o dividendo? Emita outro título.

**Fim do jogo:** quando **6 cidades** estiverem abandonadas (solo: 5).
Joga-se mais 1 turno completo e para.

**Pontuação:** posição na trilha de renda **− 1 por título**. Mais PV vence.
Empate: mais cidades com ligação; depois, mais dinheiro.

---

## 6. SOLO

Mesma coisa, sem disputa de bônus: você marca todos os bônus de primeira entrega.
Duração fixa: **12 turnos**. Metas:

- 40 PV — *Chefe de Estação*
- 55 PV — *Barão*
- 70 PV — *Lorde dos Trilhos*

---

## 7. MOTOR

Nível 1 a 5. Nível = alcance máximo de uma entrega (em hexágonos).

| P/ subir para | 2 | 3 | 4 | 5 |
|---|---|---|---|---|
| Custo (mil) | 8 | 12 | 16 | 20 |

Começa no nível 1. Sobe 1 nível por ação.

---

## 8. EM ABERTO (a decidir com testes)

- Leilão de primeiro jogador (o original tem; em 2 jogadores pode ser cruel ou ótimo).
- Se o garfo deve custar 2 formas **ou** 1 forma + 3 mil.
- Se o motor deve limitar também quantas peças se desenha por turno.
- Bônus de cidade: 3/4 fixos ou escalando com a distância até o centro.


