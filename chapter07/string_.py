import unicodedata

def unicode_test(value):
    name = unicodedata.name(value)
    value2 = unicodedata.lookup(name)
    print('value="%s", name="%s", value2="%s"'
            % (value, name, value2))

unicode_test('A')
unicode_test('$')
unicode_test('\u00a2')
unicode_test('\u20ac')
unicode_test('\u2603')

print(unicodedata.name('\u00e9'))
print(unicodedata.lookup('LATIN SMALL LETTER E WITH ACUTE'))

place = 'caf\u00e9'
print(place)

place = 'caf\N{LATIN SMALL LETTER E WITH ACUTE}'
print(place)

u_umlaut = '\N{LATIN SMALL LETTER U WItH DIAERESIS}'
print(u_umlaut)

drink = 'Gew' + u_umlaut + 'rztraminer'
print('Now I can finally have my', drink, 'in a', place)

print(len('$'))
print(len('\U0001f47b'))

snowman = '\u2603'
print(len(snowman))

ds = snowman.encode('utf-8')
print(len(ds))
print(ds)

#  ds = snowman.encode('ascii')

print(snowman.encode('ascii', 'ignore'))
print(snowman.encode('ascii', 'replace'))
print(snowman.encode('ascii', 'backslashreplace'))
print(snowman.encode('ascii', 'xmlcharrefreplace'))

place = 'caf\u00e9'
print(place)
print(type(place))

place_bytes = place.encode('utf-8')
print(place_bytes)
print(type(place_bytes))

place2 = place_bytes.decode('utf-8')
print(place2)

#  place3 = place_bytes.decode('ascii')

place4 = place_bytes.decode('latin-1')
print(place4)
place5 = place_bytes.decode('windows-1252')
print(place5)

