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
