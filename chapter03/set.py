empty_set = set()
print(empty_set)

even_numbers = {0, 2, 4, 6, 8}
print(even_numbers)

odd_numbers = {1, 3, 5, 7, 9}
print(odd_numbers)

print(set('letters'))

print(set(['Dascer', 'Dasher', 'Prancer', 'Mason-Dixon']))

print(set(('Ummagumma', 'Echoes', 'Atom Heat Mother')))

dict = {'a': 1, 'b': 2, 'c': 3}
print(set(dict))

drinks = {
        'martini': {'vodka', 'vermouth', 'a', 'b', 'c', 'd'},
        'black russian': {'vodka', 'vermouth', 'a', 'b', 'c'}
        }
print(drinks)
for name, contents in drinks.items():
    if 'vodka' in contents:
        print(name)
for name, contents in drinks.items():
    if contents and not ('vermouth' in contents or 'cream' in contents):
        print(name)
for name, contents in drinks.items():
    if contents & {'vodka', 'kahlua'}:
        print(name)

bruss = drinks['black russian']
wruss = drinks['martini']
print(bruss & wruss)
print(bruss | wruss)
print(bruss - wruss)
print(bruss ^ wruss)
print(bruss <= wruss)
print(bruss < wruss)

marxes = ['Groucho', 'Chico', 'Harpo']
pythons = ['Chapman', 'Cleese', 'Cilliam', 'Jones', 'Palin']
stooges = ['Moe', 'Curly', 'Larry']

tuple_of_lists = marxes, pythons, stooges
print(tuple_of_lists)

list_of_lists = [marxes, pythons, stooges]
print(list_of_lists)

dict_of_lists = {'Marxes': marxes, 'Pythons': pythons, 'Stooges': stooges}
print(dict_of_lists)

houses = {
        (1, 2, 3): 'My House',
        (1, 2, 4): 'The White House'
        }
print(houses)
