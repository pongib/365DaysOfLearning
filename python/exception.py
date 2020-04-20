import sys
import random
# sys.argv[0] is file name 
# sys.argv[1] is argument

# run with python3 exception.py xxx yyy zzz
try:
    print(f'input is {sys.argv[1]}')
    print(f'length {len(sys.argv)}')
    if len(sys.argv) < 3:
        raise Exception('Need to put more keyword.')
    args = sys.argv
    random.shuffle(args)
    print(f'random is {args[0]}')
except (IndexError, KeyError) as err:
    print(f'err is {err}')
    # sys.exit(1)
except NameError:
    print(f'Not found random module.')
    # sys.exit(1)
except Exception as err:
    print(f'Last error is {err}')
    raise err
else: # kind of happy path that error don't occur
    print('This is else')
finally:
    print('This is finally')