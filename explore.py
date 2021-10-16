import os

print(1 << 0)
print(1 << 1)
print(1 << 2)

print(bin(1 << 0)[2:])
print(bin(1 << 1)[2:])
print(bin(1 << 2)[2:])

nums = [1, 2, 3]
b = [4, 5, 6]
print(nums + b)

nums = []
b = [[1, 2, 3], [4, 5, 6]]
print(nums + b)

nums = [[1, 2, 3], [4, 5, 6]]
b = [[7, 8, 9], [10, 11, 12]]
print(nums + b)

nums = [[]]
b = [[1, 2, 3], [4, 5, 6]]
print(nums + b)

nums = []
b = [1, 2, 3]
print(nums + b)

nums = []
b = [[1, 2, 3]]
print(nums + b)

s = ' hello  world'
s = s.strip()
print(s)

print(0 * '0' + 'abc')

print(ord('Z'))
print(ord('Z') - ord('A'))

data = [{'a': 1, 'b': 2}, {'a': 3, 'd': 4}, {'e': 5, 'a': 6}]

print(sorted(data, key=lambda x: x['a']))

print(None and False)
