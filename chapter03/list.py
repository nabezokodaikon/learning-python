empty_list = []
weekdays = ['Monday', 'Tuesday']
another_empty_list = list()
print(another_empty_list)
print(list('cat'))

a_tuple = ('ready', 'fire', 'aim')
print(list(a_tuple))

birthday = '1/6/1952'
print(birthday.split('/'))

marxes = ['Groucho', 'Chico', 'Harpo']
print(marxes[-2])
print(marxes[-3])
print(marxes[:2])
print(marxes[1:2])
print(marxes[::2])
marxes.append('Zeppo')
print(marxes)

del marxes[-1]
print(marxes)

print(', '.join(marxes))

a = [1, 2, 3]
print(a)
b = a.copy()
print(b)
c = list(a)
print(c)
d = a[:]
print(d)
