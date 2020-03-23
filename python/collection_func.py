from functools import reduce
# Map
# f(x) = x * 2
domain = [1, 2, 3, 4, 5]

double_num = map(lambda num: num * 2, domain)
print(list(double_num))

odds = filter(lambda num: num % 2 != 0, domain)
print(list(odds))


sum = reduce(lambda acc, num: acc + num, domain, 0)
print(sum)

names = ['A', 'man', 'In', 'The', 'middle']
print('Default sorted')
print(sorted(names))

print('Lambda sorted')
print(sorted(names, key=lambda s: s.lower()))

print('Lambda sorted with reverse')
print(sorted(names, key=lambda s: s.lower(), reverse=True))

# Can call with str type follow with method
print('My_String'.lower() == str.lower('My_String'))

print('Sorted with method')
names.sort(key=str.lower, reverse=True)
print(names)