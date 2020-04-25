# use for acquire and release resource of os.
# in our create class use with __enter__ for acquire
# and __exit__ for release resource.
# REF: https://www.geeksforgeeks.org/with-statement-in-python/
# https://docs.python.org/2.5/whatsnew/pep-343.html

class MessageWriter():
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        print('__enter__')
        self.open_file = open(self.filename, 'w+')
        # this self.open_file is called resource descriptor
        return self.open_file

    # after code executed complete it will call __exit__ 
    # auto for release resource. And it take 4 parameter.
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('__exit__')
        self.open_file.close()

    # __enter__ and __exit__ are called context manager.

# f here is resource descriptor from __enter__
with MessageWriter('pongtsu.txt') as f:
    f.write('pongtsu\n')
# after executed f.write complete it call __exit__ for release resource.
