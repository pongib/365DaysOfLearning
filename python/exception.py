import sys
import random
# sys.argv[0] is file name 
# sys.argv[1] is argument

# run with python3 exception.py xxx yyy zzz
try:
    print(f'input is {sys.argv[1]}')
    args = sys.argv
    random.shuffle(args)
    print(f'random is {args[0]}')
except (IndexError, KeyError) as err:
    print(f'err is {err}')
    # sys.exit(1)
except NameError:
    print(f'Not found random module.')
    # sys.exit(1)
except:
    print('Last error')
else: # kind of happy path that error don't occur
    print('This is else')
finally:
    print('This is finally')