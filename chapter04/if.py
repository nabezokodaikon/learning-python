disaster = True
if disaster:
    print('Woe!')
else:
    print('Whee!')

furry = True
small = True
if furry:
    if small:
        print('It\'s a cat.')
    else:
        print("It's a bear!")
else:
    if small:
        print("It's a skink!")
    else:
        print("It's a human. Or a hairless bear.")

color = "puce"
if color == "red":
    print("It's a tomato")
elif color == "green":
    print("It's green pepper")
elif color == "bee purple":
    print("I don't know what it is, but only bees can see it")
else:
    print("I've never head of the color", color)

some_list = []
if some_list:
    print("There's something in here")
else:
    print("Hey, it's empty!")
