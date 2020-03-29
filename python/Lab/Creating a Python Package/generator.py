from random import sample

# Do not modify or remove this
with open("/usr/share/dict/words", "r") as f:
    WORD_LIST = [w.strip("\n") for w in f.readlines()]

def random_word():
    return sample(WORD_LIST, 10)[0]

def random_words(num):
    return sample(WORD_LIST, num)[:num]

