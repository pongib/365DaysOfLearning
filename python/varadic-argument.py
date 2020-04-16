def test(*args, **kwargs):
    print(args)
    print(kwargs)


def not_convention(*required, **optional):
    print(required)
    print(optional)

test('asdf', 'cvccc', 'asdfasdf', name='pong', namex='gib')
# ('asdf', 'cvccc', 'asdfasdf')
# {'name': 'pong', 'namex': 'gib'}
not_convention('aaa', 'bbb', 'ccc', name='pong', namex='gib')
# ('aaa', 'bbb', 'ccc')
# {'name': 'pong', 'namex': 'gib'}



from functools import reduce

primes = [2, 3, 5, 7, 11, 13]

def product(*numbers):
    print(numbers)
    p = reduce(lambda x, y: x * y, numbers)
    return p 

print(product(*primes))
# 30030

print(product(primes))
# [2, 3, 5, 7, 11, 13]



# dict use **

headers = {
    'Accept': 'text/plain',
    'Content-Length': 348, 
    'Host': 'http://mingrammer.com' 
}  

def pre_process(**headers): 
    content_length = headers['Content-Length'] 
    print('content length: ', content_length) 
    
    host = headers['Host']
    if 'https' not in host: 
        raise ValueError('You must use SSL for http communication')  
        
pre_process(**headers)



# content length:  348
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "<stdin>", line 7, in pre_process
# ValueError: You must use SSL for http communication



numbers = [1, 2, 3, 4, 5, 6]

# The left side of unpacking should be list or tuple.
*a, = numbers
# a = [1, 2, 3, 4, 5, 6]

*a, b = numbers
# a = [1, 2, 3, 4, 5]
# b = 6

a, *b, = numbers
# a = 1 
# b = [2, 3, 4, 5, 6]

a, *b, c = numbers
# a = 1
# b = [2, 3, 4, 5]
# c = 6