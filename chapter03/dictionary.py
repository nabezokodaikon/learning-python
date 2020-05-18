empty_dict = {}
print(empty_dict)

bierce = {
        "day": "A",
        "positive": "B",
        "misfortune": "C"
        }
print(bierce)

lol = [['a', 'b'], ['c', 'd'], ['e', 'f']]
print(dict(lol))

lol = [('a', 'b'), ('c', 'd'), ('e', 'f')]
print(dict(lol))

bierce['g'] = 'h'
print(bierce)

pythons = {
        'Chapman': 'Graham',
        'Cleese': 'John',
        'Idle': 'Eric',
        'Jones': 'Terry',
        'Palin': 'Michael'
        }
others = {
        'Marx': 'Groucho',
        'Howard': 'Moe'
        }
pythons.update(others)
print(pythons)

del pythons['Marx']
print(pythons)

#  pythons.clear()
#  print(pythons)

print('Palin' in pythons)
print('X' in pythons)

print(pythons['Cleese'])

print(pythons.get('Cleese'))
print(pythons.get('a', 'Not a Python'))
print(pythons.get('a'))
print(pythons.keys())

signals = {
        'green': 'go',
        'yellow': 'go faster',
        'red': 'ismile for the camera'
        }
print(signals.keys())

print(signals.values())
print(list(signals.values()))

print(list(signals.items()))

original_signals = signals.copy()
original_signals['blue'] = 'confuse everyone'
print(signals)
print(original_signals)

print('\n')

save_signals = signals
signals['blue'] = 'confuse everyone'
print(signals)
print(save_signals)
