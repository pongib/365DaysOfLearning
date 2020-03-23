# if CONDITION:
#     my_var = 1
# else:
#     my_var = 2

# ## Can flatten to

# my_var = 1 if CONDITION else 2

# ## IF dont want to return can be

# print('a') if CONDITION else print('b')

my_age = False if True else 20
my_other_age = 30 if False else False
my_var = my_age or my_other_age or 21
my_and = my_age and 21
print(my_age)
print(my_other_age)
print(my_var)
print(my_and)