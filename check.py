import sys
text = open('patch_theory_aie.py', encoding='utf-8').read()
quotes = []
idx = 0
while True:
    idx = text.find('"""', idx)
    if idx == -1: break
    quotes.append(idx)
    idx += 3

print("Total triple quotes:", len(quotes))
for i in range(0, len(quotes), 2):
    if i+1 < len(quotes):
        print(f"String from char {quotes[i]} to {quotes[i+1]}")
    else:
        print(f"Unclosed string starting at char {quotes[i]}")

