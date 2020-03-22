x = 5

def set_y(y):    
    global x
    x = y    
    y = x    
    global z
    z = 99
    print('inner x', x)
    print('inner y', y)
    
  
print('x before set', x)
set_y(10)
print('x after set', x)
print('z is ', z)
while x < 6:
    print(x)
    x += 1


print('Outter x', x)