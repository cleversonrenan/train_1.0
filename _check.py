import re, sys

f = sys.argv[1]
s = open(f, encoding="utf-8").read()
xs = [float(v) for v in re.findall(r'(?:x|x1|x2|cx)="(-?[\d.]+)"', s)]
ys = [float(v) for v in re.findall(r'(?:y|y1|y2|cy)="(-?[\d.]+)"', s)]
print(f, "| elementos:", s.count("<"),
      "| x:", round(min(xs), 1), "->", round(max(xs), 1),
      "| y:", round(min(ys), 1), "->", round(max(ys), 1),
      "| nan:", "nan" in s.lower())
