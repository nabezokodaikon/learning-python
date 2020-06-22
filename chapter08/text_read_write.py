poem = '''There was a young lady named Bright,
Whose speed was far faster than light;
She statted one day
In a relative way,
And returned on previous night.'''
print(len(poem))

fout = open('relativity', 'wt')
fout.write(poem)
fout.close()

fout = open('relativity2', 'wt')
print(poem, file=fout)
fout.close()

fout = open('relativity', 'wt')
size = len(poem)
offset = 0
chunk = 2
while True:
    if offset > size:
        break
    print(fout.write(poem[offset:offset + chunk]))
    offset += chunk
fout.close()

#  fout = open('relativity', 'xt')
from builtins import FileExistsError
try:
    fout = open('relativity', 'xt')
    fout.write('stomp stomp stomp')
except FileExistsError:
    print('relativity already exists!. That was a close one.')

fin = open('relativity', 'rt')
poem = fin.read()
fin.close()
print(len(poem))

poem = ''
fin = open('relativity', 'rt')
chunk = 100
while True:
    fragment = fin.read(chunk)
    if not fragment:
        break
    poem += fragment

fin.close()
print(len(poem))

if not 1:
    print('not 0')
else:
    print('0')

poem = ''
fin = open('relativity', 'rt')
while True:
    line = fin.readline()
    if not line:
        break
    poem += line

fin.close()
print(len(poem))

poem = ''
fin = open('relativity', 'rt')
for line in fin:
    poem += line

fin.close()
print(len(poem))

fin = open('relativity', 'rt')
lines = fin.readlines()
fin.close()
print(len(lines), 'lines read')
for line in lines:
    print(line, end='')
