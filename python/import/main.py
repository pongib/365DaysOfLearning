# import helpers
# import helpers as h
from helpers import *
# can still import private
from helpers import _extract_lower_sorted
# Explicit is better to avoid collsion name entity.
# from helpers import (
#     extract_lower_sorted, extract_upper_sorted_reversed as e_up, my_name
# )

from another import *

print(f'__name__ on main is {__name__}')

name = "Sittipong SripaisaRnMonGKoL"
print(f"Lower is {_extract_lower_sorted(name)}")
print(f"Upper is {extract_upper_sorted_reversed(name)}")
print(f"From Name var Lower is {_extract_lower_sorted(my_name)}")