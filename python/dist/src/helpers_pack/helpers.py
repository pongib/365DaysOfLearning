def extract_lower_sorted(name):
    return list(sorted(filter(str.islower, name)))

def extract_upper_sorted_reversed(name):
    return list(sorted(filter(str.isupper, name), reverse=True))