import json, glob
files = glob.glob('curriculum/tracks/*.json')
targets = ['c_cpp', 'csharp', 'cybersecurity', 'devops', 'go', 'mobile', 'php', 'ruby', 'rust', 'software']

for f in files:
    if any(x in f for x in targets):
        d = json.load(open(f, encoding='utf-8'))
        print(f, len(d.keys()))
