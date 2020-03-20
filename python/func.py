# 1) Write a `split_name` function that takes a string and returns a dictionary with first_name and last_name

def split_name(name):
    return {
        'first_name': name.split(' ')[0],
        'last_name': ' '.join(name.split(' ')[1:]),
    }

# solution
# def split_name(name):
#     first_name, last_name = name.split(maxsplit=1)
#     return {
#         'first_name': first_name,
#         'last_name': last_name,
#     }
    

assert split_name("Kevin Bacon") == {
    "first_name": "Kevin",
    "last_name": "Bacon",
}, f"1.Expected {{'first_name': 'Kevin', 'last_name': 'Bacon'}} but received {split_name('Kevin Bacon')}"

# 2) Ensure that `split_name` can handle multi-word last names

assert split_name("Victor Von Doom") == {
    "first_name": "Victor",
    "last_name": "Von Doom",
}, f"2.Expected {{'first_name': 'Victor', 'last_name': 'Von Doom'}} but received {split_name('Victor Von Doom')}"

# 3) Write an `is_palindrome` function to check if a string is a palindrome (reads the same from left-to-right and right-to-left)

def is_palindrome(word):
    word = str(word)
    length_word = len(word)    
    if length_word % 2 != 0:
        return list(word)[:int(length_word/2)][::-1] == list(word)[int(length_word/2)+1:]
    else:
        return list(word)[:int(length_word/2)][::-1] == list(word)[int(length_word/2):]

# solution it very hurt.
# def is_palindrome(item):
#     item = str(item)
#     return item == item[::-1]
    
        
assert is_palindrome("radar") == True, f"3.Expected True but got {is_palindrome('radar')}"
assert is_palindrome("radum") == False, f"3.Expected False but got {is_palindrome('radum')}"
assert is_palindrome("stop") == False, f"3.Expected False but got {is_palindrome('stop')}"
assert is_palindrome("abba") == True, f"3.Expected True but got {is_palindrome('abba')}"

# 4) Make `is_palindrome` work with numbers

assert is_palindrome(101) == True, f"4.Expected True but got {is_palindrome(101)}"
assert is_palindrome(10) == False, f"4.Expected False but got {is_palindrome(10)}"

# 5) Write a `build_list` function that takes an item and a number to include in a list

def build_list(item, number=1):
    return [item for _ in range(number)]

# solution
# def build_list(item, count=1):
#     items = []
#     for _ in range(count):
#         items.append(item)
#     return items

assert build_list("Apple", 3) == [
    "Apple",
    "Apple",
    "Apple",
], f"5.Expected ['Apple', 'Apple', 'Apple'] but received {repr(build_list('Apple', 3))}"
assert build_list("Orange") == [
    "Orange"
], f"5.Expected ['Orange'] but received {repr(build_list('Orange'))}"

print('Success!')