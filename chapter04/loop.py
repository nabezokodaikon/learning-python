#  count = 1
#  while count <= 5:
#  print(count)
#  count += 1

#  while True:
#  stuff = input("String to capitalize [type q to quit]: ")
#  if stuff == "q":
#  break
#  print(stuff.capitalize())

#  while True:
#  value = input('Integer, please [q to quit]')
#  if value == 'q':
#  break
#  number = int(value)
#  if number % 2 == 0:
#  continue
#  print(number, 'squared is', number * number)

numbers = [1, 3, 5]
position = 0
while position < len(numbers):
    number = numbers[position]
    if number % 2 == 0:
        print('For even number', number)
        break
    position += 1
else:
    print('No even number found')

rabbits = ['Flopsy', 'Mopsy', 'Cottontail', 'Peter']
current = 0
while current < len(rabbits):
    print(rabbits[current])
    current += 1

for rabbit in rabbits:
    print(rabbit)

word = 'cat'
for letter in word:
    print(letter)

accusation = {'room': 'ballroom', 'weapon': 'lead pipe',
              'person': 'Col. Mustard'}
for card in accusation:
    print(card)

for value in accusation.values():
    print(value)

for item in accusation.items():
    print(item)

for card, contents in accusation.items():
    print('Card', card, 'has the contents', contents)

cheeses = []
for cheese in cheeses:
    print('This shop has some lovely', cheese)
    break
else:
    print('This is not much of a cheese shop, items it?')

found_one = False
for cheese in cheeses:
    found_one = True
    print('This shop has some lovely', cheese)
    break

if not found_one:
    print('This is not much of a cheese shop, items it?')

days = ['Monday', 'Thesday', 'Wednesday']
fruits = ['banana', 'orange', 'peach']
drinks = ['coffee', 'tea', 'beer']
desserts = ['tiramisu', 'ice creditsam', 'pie', 'pudding']
for day, fruit, drink, dessert in zip(days, fruits, drinks, desserts):
    print(day, ': drink', drink, '- eat', fruit, '- enjoy', dessert)

english = 'Monday', 'Tuesday', 'Wednesday'
french = 'Lundi', 'Mardi', 'Mercredi'
print(list(zip(english, french)))
print(dict(zip(english, french)))

for x in range(0, 3):
    print(x)

print(list(range(0, 3)))

print(list(range(2, -1, -1)))

print(list(range(0, 11, 2)))
