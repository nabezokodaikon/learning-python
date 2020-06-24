import csv

villains = [
        ['Doctor', 'No'],
        ['Rosa', 'Klebb'],
        ['Mister', 'Big'],
        ['Auric', 'Goldfinger'],
        ['Ernst', 'Blofeld']
        ]
with open('villains.csv', 'wt') as fout:
    csvout = csv.writer(fout)
    csvout.writerows(villains)

with open('villains.csv', 'rt') as fin:
    cin = csv.reader(fin)
    villains = [row for row in cin]
print(villains)

with open('villains.csv', 'rt') as fin:
    cin = csv.DictReader(fin, fieldnames=['first', 'last'])
    villains = [row for row in cin]
print(villains)

villains = [
        {'first': 'Doctor', 'last': 'No'},
        {'first': 'Rosa', 'last': 'Klebb'},
        {'first': 'Mister', 'last': 'Big'},
        {'first': 'Auric', 'last': 'Goldfinger'},
        {'first': 'Ernst', 'last': 'Blofeld'},
        ]
with open('villains.csv', 'wt') as fout:
    cout = csv.DictWriter(fout, fieldnames=['first', 'last'])
    cout.writeheader()
    cout.writerows(villains)

with open('villains.csv', 'rt') as fin:
    cin = csv.DictReader(fin)
    villains = [row for row in cin]
print(villains)
