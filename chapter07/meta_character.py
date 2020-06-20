import re

source = '''I wish I may, I wish I might
... Have a dish of fish tonight.'''

print(re.findall('wish', source))

print(re.findall('wish|fish', source))

print(re.findall('^wish', source))

print(re.findall('^I wish', source))

print(re.findall('fish$', source))

print(re.findall('fish tonight\.$', source))

print(re.findall('[wf]ish', source))

print(re.findall('[wsh]+', source))

print(re.findall('ght\W', source))

print(re.findall('I (?=wish)', source))

print(re.findall('(?<=I) wish', source))

print(re.findall(r'\bfish', source))

m = re.search(r'(. dish\b).*(\bfish)', source)
print(m.group())
print(m.groups())

m = re.search(r'(?P<DISH>. dish\b).*(?P<FISH>\bfish)', source)
print(m.group())
print(m.groups())
print(m.group('DISH'))
print(m.group('FISH'))
