from random import sample

# Do not modify or remove this
with open("/Users/pongtsu/Documents/work/learn/365DaysOfLearning/python/Lab/Creating a Python Package/words", "r") as f:
    WORD_LIST = [w.strip("\n") for w in f.readlines()]

def random_word():
    return sample(WORD_LIST, 10)[0]


def random_words(length):
    return sample(WORD_LIST, length) 