"""
This is function in helpers package
"""
# use docstring with extract_lower_sorted.__doc__
# use doctest with python3 -m doctest src/helpers_pack/helpers.py
def extract_lower_sorted(name):
    # intent doctest to fail
    # correct is ['a', 'c', 'd', 'f']
    """
    Here is description of extrack lower with sorted and have test

    >>> extract_lower_sorted('BcdEfaG')
    ['a', 'c', 'd', 'f', 'x']
    """
    return list(sorted(filter(str.islower, name)))

def extract_upper_sorted_reversed(name):
    return list(sorted(filter(str.isupper, name), reverse=True))