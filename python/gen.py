# function like range(10)
def gen_range(stop, start=0, step=1):
    while start < stop:
        yield start
        start += step

# name = 'pongtsu'
# arr = [name for _ in gen_range(10)]
# print(arr)

# can use python3 -i gen.py to run repl with this gen_range function

def gen_fibo():
    a, b = 0, 1    
    while True:
        a, b = b, a + b
        yield a
        