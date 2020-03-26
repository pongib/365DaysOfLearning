# private method
def _extract_lower_sorted(name):
    return list(sorted(filter(str.islower, name)))

def extract_upper_sorted_reversed(name):
    return list(sorted(filter(str.isupper, name), reverse=True))

my_name = 'ponGtsu'

# allow only this name method
# __all__ = ['extract_upper_sorted_reversed']

# Execute if it a main script file or use -m to run this module 
# -m short from module
if __name__ == '__main__':
    print('HELPERS is MAIN !!!!!!')