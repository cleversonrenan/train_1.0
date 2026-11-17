# -*- coding: utf-8 -*-
"""Reparo definitivo: bytes -> decode utf-8 (tz. BOM) -> desfaz mojibake cp1252."""
import os

MARKERS = ("Ã", "â€", "Â°")


def to_bytes(s):
    out = bytearray()
    for ch in s:
        o = ord(ch)
        if o < 0x100:
            out.append(o)
        else:
            out += ch.encode("cp1252")
    return bytes(out)


for path in ["REGRAS_v0.2.md", "gerar_folha.py"]:
    raw = open(path, "rb").read()
    if raw.startswith(b"\xef\xbb\xbf"):
        raw = raw[3:]
    s = raw.decode("utf-8")
    if any(m in s for m in MARKERS):
        s = to_bytes(s).decode("utf-8")
        print("reparado:", path)
    open(path, "w", encoding="utf-8", newline="\n").write(s)
    print(path, "| mojibake:", any(m in s for m in MARKERS))
