x = 5

def set_y(y):    
    x = y    
    y = x        
    print('inner x', x)
    print('inner y', y)
    
  

set_y(10)

while x < 6:
    print(x)
    x += 1

print('Outter x', x)