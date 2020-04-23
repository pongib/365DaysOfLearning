class DoubleTwo:
    def __init__(self, max = 0):
        self.max = max
    
    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.max:
            result = 2 ** self.n
            self.n = self.n + 1
            return result
        else:
            raise StopIteration

# run with this command
# >>> double = DoubleTwo(5)
# >>> result = iter(double)
# >>> next(result)
# 1
# >>> next(result)
# 2
# >>> next(result)
# 4
# >>> next(result)
# 8
# >>> next(result)
# 16
# >>> next(result)
# 32
# >>> next(result)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "iterable.py", line 15, in __next__
#     raise StopIteration
# StopIteration