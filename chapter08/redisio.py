import redis
conn = redis.Redis()

conn.keys('*')
print(conn.set('secret', 'ni!'))
print(conn.set('carats', 24))
print(conn.set('fever', '101.5'))

print(conn.get('secret'))
print(conn.get('carats'))
print(conn.get('fever'))

print(conn.setnx('secret', 'icky-icky-icky-ptang-zoop-boing!'))

print(conn.getset('secret', 'icky-icky-icky-ptang-zoop-boing!'))
print(conn.get('secret'))

print(conn.getrange('secret', -6, -1))

print(conn.setrange('secret', 0, 'ICKY'))
print(conn.get('secret'))
