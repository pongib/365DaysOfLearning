my_file = open('car.txt', 'w')
my_file.write('Ferari\n')
my_file.write('Toyota\n')
my_file.writelines([
    'Audi\n',
    'Porche\n',    
])