# my_file = open('car.txt', 'w+')
with open('car.txt', 'r+b') as my_file:
    print(my_file.read())
    my_file.seek(0)
    print(my_file.readlines())
    my_file.write(b'BMW\n')
    my_file.write(b'\x10')
    print(my_file.readlines())



with open('car.txt', 'r+b') as my_file:
    b_array = bytearray(range(10))
    my_file.readinto(b_array)
    print(b_array)
    my_file.seek(0)
    new_b_array = bytearray(my_file.read(10))
    print(new_b_array == b_array)
