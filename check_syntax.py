# -*- coding: utf-8 -*-
import ast, sys

with open('enrich_batch2.py', encoding='utf-8') as f:
    src = f.read()
try:
    ast.parse(src)
    print('Syntax OK!')
except SyntaxError as e:
    print(f'Error on line {e.lineno}: {e.msg}')
    lines = src.splitlines()
    # Show 10 lines of context before the error
    start = max(0, e.lineno - 12)
    end = min(len(lines), e.lineno + 3)
    for i, line in enumerate(lines[start:end], start + 1):
        marker = ' >>>' if i == e.lineno else '    '
        print(f'{marker} {i}: {line[:120]}')
