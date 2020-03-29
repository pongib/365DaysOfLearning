from random import shuffle as l_shuffle

def reverse(name):
    return name[::-1]

def shuffle(name):
    l_name = list(name)
    l_shuffle(l_name)
    return "".join(l_name)
    