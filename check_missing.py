import json
import glob

with open('backend_stubs.txt', 'r', encoding='utf-16le') as f:
    stubs = [line.split('"')[1] for line in f if '"' in line]

done = set()
for file in glob.glob('theory_data/backend*.json'):
    with open(file, 'r', encoding='utf-8') as f:
        data = json.load(f)
        done.update(data.keys())

missing = [s for s in stubs if s not in done]
print('Missing:', len(missing))
for m in missing:
    print('-', m)
