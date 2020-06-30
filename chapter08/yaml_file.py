import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), 'site-packages'))

import yaml
with open('mcintyre.yaml', 'rt') as fin:
    text = fin.read()

data = yaml.load(text)
print(data['details'])
print(len(data['poems']))
print(data['poems'][1]['title'])
