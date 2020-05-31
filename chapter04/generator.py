print(sum(range(1, 100)))

def my_range(first = 0, last = 100, step = 1):
    number = first
    while number < last:
        yield number
        number += step

print(my_range)

print(sum(my_range(1, 5)))

for x in my_range(1, 5):
    print(x)
