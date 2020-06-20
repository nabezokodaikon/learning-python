blist = [1, 2, 3, 255]
the_bytes = bytes(blist)
print(the_bytes)
the_bytes_array = bytearray(blist)
print(the_bytes_array)

print(b'\x61')
print(b'\x01abc\xff')

#  the_bytes[1] = 127
the_bytes_array[1] = 127
print(the_bytes_array)

the_bytes = bytes(range(0, 256))
the_bytes_array = bytearray(range(0, 256))
print(the_bytes)
print(the_bytes_array)

import struct
print(struct.pack('>L', 154))
print(struct.pack('>L', 141))
