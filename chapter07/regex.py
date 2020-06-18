import re
source = 'Young Frankenstein'
m = re.match('You', source)
if m:
    print(m.group())

m = re.match('^You', source)
if m:
    print(m.group())

m = re.search('Frank', source)
if m:
    print(m.group())

m = re.match('.*Frank', source)
if m:
    print(m.group())

m = re.search('Frank', source)
if m:
    print(m.group())

m = re.findall('n', source)
print('Found', len(m), 'matches')

m = re.findall('n.', source)
print(m)

m = re.findall('n.?', source)
print(m)

m = re.split('n', source)
print(m)

m = re.sub('n', '?', source)
print(m)

import string
printable = string.printable
print(len(printable))
print(printable[0:50])
print(printable[50:])

print(re.findall('\d', printable))
print(re.findall('\w', printable))
print(re.findall('\s', printable))

x = 'abc' + '-/*' + '\u00ea' + '\u0115'
print(re.findall('\w', x))
