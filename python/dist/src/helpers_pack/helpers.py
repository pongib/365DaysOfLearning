"""
This is function in helpers package
"""

def extract_lower_sorted(name):
    """
    Here is description of extrack lower with sorted and have test

    >>> extract_lower_sorted('BcdEfaG')
    ['a', 'c', 'd', 'f']
    """
    return list(sorted(filter(str.islower, name)))

def extract_upper_sorted_reversed(name):
    return list(sorted(filter(str.isupper, name), reverse=True))