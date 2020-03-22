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