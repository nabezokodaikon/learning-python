peridic_table = {'Hydrogen': 1, 'Helium': 2}
print(peridic_table)

carbon = peridic_table.setdefault('Carbon', 12)
print(carbon)
print(peridic_table)

helium = peridic_table.setdefault('Helium', 947)
print(helium)
print(peridic_table)

from collections import defaultdict
peridic_table = defaultdict(int)

peridic_table['Hydrogen'] = 1
print(peridic_table['Lead'])
print(peridic_table)

def no_idea():
    return 'Huh?'

bestiary = defaultdict(no_idea)
bestiary['A'] = 'Abominable Snowman'
bestiary['B'] = 'Basilisk'
print(bestiary['A'])
print(bestiary['B'])
print(bestiary['C'])

bestiary = defaultdict(lambda: 'Huh?')
print(bestiary['E'])

food_counter = defaultdict(int)
for food in ['spam', 'spam', 'eggs', 'spam']:
    food_counter[food] += 1

for food, count in food_counter.items():
    print(food, count)

dict_counter = {}
for food in ['spam', 'spam', 'eggs', 'spam']:
    if not food in dict_counter:
        dict_counter[food] = 0
    dict_counter[food] += 1

for food, count in dict_counter.items():
    print(food, count)

from collections import Counter
breakfast = ['spam', 'spam', 'eggs', 'spam']
breakfast_counter = Counter(breakfast)
print(breakfast_counter)

print(breakfast_counter.most_common())
print(breakfast_counter.most_common(1))

lunch = ['eggs', 'eggs', 'bacon']
lunch_counter = Counter(lunch)
print(lunch_counter)

print(breakfast_counter + lunch_counter)
print(breakfast_counter - lunch_counter)
print(lunch_counter - breakfast_counter)
print(breakfast_counter & lunch_counter)
print(breakfast_counter | lunch_counter)
