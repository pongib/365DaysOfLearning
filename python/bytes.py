my_bytes = b'This is byte'
bytes(10)
bytes(range(10))
b'\x09'
my_bytes[0]
my_bytes[0:1]

bytearray(10)
bytearray(range(10))
my_bytes = bytearray(b'THIS is byte')
my_bytes[0]
my_bytes[0:1]
my_bytes[0:1] = b'E'
my_bytes[0] = 0x11