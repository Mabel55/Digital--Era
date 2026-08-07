# -*- coding: utf-8 -*-
import ast

with open('enrich_batch2.py', encoding='utf-8') as f:
    src = f.read()

# Try full parse
try:
    ast.parse(src)
    print('FULL FILE: Syntax OK!')
except SyntaxError as e:
    print(f'FULL FILE ERROR at line {e.lineno}: {e.msg}')
    lines = src.splitlines()
    start = max(0, e.lineno - 8)
    end = min(len(lines), e.lineno + 3)
    for i in range(start, end):
        marker = '>>>' if i+1 == e.lineno else '   '
        safe = lines[i].encode('ascii', 'replace').decode()[:90]
        print(f'{marker} {i+1}: {safe}')
