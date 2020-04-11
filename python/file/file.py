# my_file = open('car.txt', 'w+')
with open('car.txt', 'w+') as my_file:
    my_file.write('Ferari\n')
    my_file.write('Toyota\n')
    my_file.writelines([
        'Audi\n',
        'Porche\n',    
    ])
# Need to move to seek 0 every read, readlines.
    my_file.seek(0)
    my_file.write('Cryler\n')
    my_file.seek(0)
    print(my_file.read())
    my_file.seek(0)
    print(my_file.readlines())
    my_file.seek(0)
    for car in my_file.readlines():
        print(car)
    
# if use with syntax no need to close file it close automatically
# my_file.close()


# my_file = open('car.txt', 'a+')
# with my_file:
#     my_file.write('Volve\n')
#     my_file.seek(0)
#     print(my_file.read())        

# my_file = open('car.txt', 'a+')
# my_file.write('Volve\n')
# my_file.seek(0)
# print(my_file.read())
# my_file.close()