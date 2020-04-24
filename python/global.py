x = 5
b = 10

def set_y(y):
    # you can reference b that outter scope here
    # but cannot reassign it because it not local scope
    # if you do it (b = 10) it wiil new assign local function scope b
    # that is not the same as b outside it called shadow or name hiding
    # description is below
    a = b
    print('inner a is', a)
    # if we use global y here 
    # will error because parameter y in set_y(y) will always win global
    global x
    # Python doesn't have variable declarations, so it has to figure out the scope of variables itself. 
    # It does so by a simple rule: If there is an assignment to a variable inside a function, that variable is considered local.
    # x += 1

    x = y
    y = x
    # can defind global z in function without defind in outter function before
    # and can be reference global z outside function as well.
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