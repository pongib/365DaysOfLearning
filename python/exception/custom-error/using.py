from cli import main
from cli.errors import CustomError

try:
    main()
except (CustomError, AssertionError) as err:
    print(f'Error is {err}')