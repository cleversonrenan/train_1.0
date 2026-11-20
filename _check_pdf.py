import pymupdf

d = pymupdf.open("Regras_Bacia_do_Corvo_v0.5.pdf")
print("paginas:", len(d), "| tamanho da pagina (pt):", d[0].rect)
for i, p in enumerate(d):
    t = p.get_text()
    print(f"--- p{i+1}: {len(t)} chars, {len(t.splitlines())} linhas")
    print("   inicio:", t.splitlines()[0][:70] if t.strip() else "(vazio)")
    print("   fim   :", t.splitlines()[-1][:70] if t.strip() else "")
full = "".join(p.get_text() for p in d)
for termo in ["Bacia do Corvo", "BIFURCAÇÃO", "Vau do Corvo", "rerrolar", "TÍTULOS", "R$"]:
    print(f"contem {termo!r}:", termo in full)
print("mojibake:", any(m in full for m in ("Ã", "â€", "Â°")))
