# form package import module
from helpers_pack import another
# import package
import helpers_pack

# test import via __init__ with hide method module
from helpers_pack import *

# form package.module import method
from helpers_pack.helpers import extract_lower_sorted


print(f"Lower is {extract_lower_sorted(another.my_name)}")
print(f"Upper is {extract_upper_sorted_reversed(another.my_name)}")
print(f"From Name var Lower is {extract_lower_sorted(another.my_name)}")
print(f"Import package {helpers_pack.helpers.extract_upper_sorted_reversed(another.my_name)}")