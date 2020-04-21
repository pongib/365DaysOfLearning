import sys

from cli.errors import CustomError

def main():

    # if len(sys.argv) < 2:
    #     raise CustomError('Input too few!')
    # print(sys.argv)
    
    # Use assert when you want program to raise exception and look way it does.
    # When use with -O flag it will skip all assert, O stand for optimize. 
    # It use when want to deploy in production
    assert len(sys.argv) < 2, f'Too much name {sys.argv}'

    print(f'Name is {sys.argv[1]}')
    return 10
