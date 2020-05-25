def do_nothing():
    pass


def make_a_sound():
    print('quick')


def agree():
    return True


def echo(anything):
    return anything + ' ' + anything


def commentary(color):
    if color == 'red':
        return "it's a tomato."
    elif color == "green":
        return "It's a green pepeer"
    elif color == "bee purple":
        return "I don't know what it is, but only bees can see it."
    else:
        return "I've never heard of the color " + color + "."


def is_none(thing):
    if thing is None:
        print("It's None")
    elif thing:
        print("It's True")
    else:
        print("It's False")


do_nothing()
make_a_sound()

if agree():
    print('Splendid!')
else:
    print('That was unexpected.')

print(echo('Rumlestiltskin'))

comment = commentary('blue')
print(comment)

thing = None
if thing:
    print("It's some thing")
else:
    print("It's no thing")

if thing is None:
    print("It's some thing")
else:
    print("It's no thing")

is_none(None)
is_none(True)
is_none(False)
is_none(0)
is_none(0.0)
is_none(())
is_none([])
is_none({})
is_none(set())


def menu(wine, entree, dessert='pudding'):
    return {'wine': wine, 'entree': entree, 'dessert': dessert}

print(menu('chardonnay', 'chicken', 'cake'))
print(menu(entree='beef', dessert='bagel', wine='bordeaux'))
print(menu('chardonnay', 'chicken'))

def buggy(arg, result=[]):
    result.append(arg)
    print(result)

buggy(111)

def works(arg):
    result = []
    result.append(arg)
    return result

print(works(111))
print(works(222))

def print_args(*args):
    print('Positional argument tuple: ', args)

print_args()
print_args(1, 2, 3)

def print_more(required1, required2, *args):
    print('Need this one: ', required1)
    print('Need this one too:', required2)
    print('All the rest:', args)

print_more(1, 2, 3, 4, 5, 6)

def print_kwargs(**kwargs):
    print('Keyword arguments: ', kwargs)

print_kwargs(wine='merlot', entree='mutton', dessert='macaroom')

def echo(anything):
    'echoは、与えられた入力引数を返す'
    return anything

#  help(echo)

print(echo.__doc__)
