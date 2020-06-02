animal = 'fruitbat'

def print_global():
    print('inside print_global:', animal)

print('at the top level:', animal)
print_global()

def change_and_print_global():
    print('inside change_and_print_global:', animal)
    #  animal = 'wombat'
    print('after the change:', animal)

change_and_print_global()

#  print(locals: {'animal': 'wombat'})

#  def change_and_print_global():
    #  global animal
    #  animal = 'wombat'
    #  print('inside change_and_print_global:', animal)

#  print(animal)

#  change_and_print_global()

#  print(animal)

animal = 'fruitbat'
def change_local():
    animal = 'wombat'
    print('locals:', locals())

print(animal)

change_local()

print('globals:', globals())

print(animal)


def amazing():
    '''これはすばらしい関数だ。
    もう一度見る?'''
    print('関数の名前:', amazing.__name__)
    print('docstring', amazing.__doc__)

amazing()
