import sys

def bar(i):
    if i == 1:
        raise KeyError(1)
    if i == 2:
        raise ValueError(2)

def bad():    
    e = None
    try:        
        bar(int(sys.argv[1]))
    except KeyError as e:        
        print('key error')        
    except ValueError as e:
        print('value error')
    print(e)

def good():    
    exception = None
    try:        
        bar(int(sys.argv[1]))
    except KeyError as e:        
        print('key error')
        exception = e
    except ValueError as e:
        print('value error')
        exception = e
    print(exception)
    
bad()