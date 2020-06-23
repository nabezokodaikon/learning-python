poem = '''There was a young lady named Bright,
Whose speed was far faster than light;
She statted one day
In a relative way,
And returned on previous night.'''

print(len(poem))
bdata = bytes(range(0, 256))
print(len(bdata))

fout = open('bfile', 'wb')
fout.write(bdata)
fout.close()

fout = open('bfile', 'wb')
size = len(bdata)
offset = 0
chunk = 2
while True:
    if offset > size:
        break
    print(fout.write(bdata[offset:offset + chunk]))
    offset += chunk
fout.close()

fin = open('bfile', 'rb')
bdata = fin.read()
print(len(bdata))
fin.close()

with open('relativity', 'wt') as fout:
    fout.write(poem)

with open('bfile', 'rb') as fin:
    print(fin.tell())
    print(fin.seek(255))

    fin.seek(255)
    bdata = fin.read()
    print(len(bdata))
    print(bdata[0])

import os
print(os.SEEK_SET)
print(os.SEEK_CUR)
print(os.SEEK_END)

with open('bfile', 'rb') as fin:
    print(fin.seek(-1, 2))
    print(fin.tell())
    bdata = fin.read()
    print(len(bdata))
    print(bdata[0])

with open('bfile', 'rb') as fin:
    print(fin.seek(254, os.SEEK_SET))
    print(fin.tell())

    print(fin.seek(1, os.SEEK_CUR))
    print(fin.tell())

    bdata = fin.read()
    print(len(bdata))
    print(bdata[0])
