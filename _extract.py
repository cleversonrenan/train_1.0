import pymupdf, glob, os, sys

for f in sorted(glob.glob("*.pdf")):
    try:
        doc = pymupdf.open(f)
        total_chars = 0
        pages = []
        for i, page in enumerate(doc):
            t = page.get_text().strip()
            total_chars += len(t)
            pages.append(t)
        print(f"{f} | pages={len(doc)} | chars={total_chars} | imgs_p0={len(doc[0].get_images())}")
        out = os.path.splitext(f)[0] + ".txt"
        with open(out, "w", encoding="utf-8") as fh:
            for i, t in enumerate(pages):
                fh.write(f"\n===== PAGE {i+1} =====\n{t}\n")
        doc.close()
    except Exception as e:
        print(f"{f} | ERROR {e}")
