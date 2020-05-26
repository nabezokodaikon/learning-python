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


def answer():
    print(42)


def run_something(func):
    func()

answer()
run_something(answer)

print(type(run_something))


def add_args(arg1, arg2):
    print(arg1 + arg2)


print(type(add_args))


def run_something_with_args(func, arg1, arg2):
    func(arg1, arg2)


run_something_with_args(add_args, 5, 9)


def sum_args(*args):
    return sum(args)


def run_with_positional_args(func, *args):
    return func(*args)


print(run_with_positional_args(sum_args, 1, 2, 3, 4))


def outer(a, b):
    def inner(c, d):
        return c + d
    return inner(a, b)

print(outer(4, 7))

def knights(saying):
    def inner(quote):
        return "We are the knights who say: '%s'" % quote
    return inner(saying)

print(knights('Ni!'))


def knights2(saying):
    def inner2():
        return "We are the knights who say: '%s'" % saying
    return inner2

a = knights2('Duck')
b = knights2('Hasenpfeffer')
print(type(a))
print(type(b))
print(a())
print(b())


def edit_story(words, func):
    for word in words:
        print(func(word))

stairs = ['thud', 'meow', 'thud', 'hiss']
def enliven(word):
    return word.capitalize() + '!'

edit_story(stairs, enliven)

edit_story(stairs, lambda word: word.capitalize() + '!')
