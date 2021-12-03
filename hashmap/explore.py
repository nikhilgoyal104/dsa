from collections import Counter
from math import inf

print(-4 % 3)

x = {'a': 4, 'b': 2}
y = {'b': 2, 'a': 4}
print(x == y)

w = 'eat'
freq = Counter(w)
print(freq)

print(ord('c') - ord('a'))

print(inf - 8)
print(abs(8 - inf))
print(abs(inf - 8))

print(8 % 2)

quot, rem = divmod(1, 2)
print(quot, rem)

a = ['1', '2', '3']
print(''.join(a))

print(-1 % 7)

s = '4 abc'

x, y = s.split(' ')
print(x, y)

subdomains = ['discuss', 'leetcode', 'com']
for i in range(len(subdomains)):
    print('.'.join(subdomains[i:]))

print(1 / 7)

nums = [1, 20, 10, 15, 3, 2]

nums = sorted(nums)
print(nums)
n = len(nums)
res = 0
for i in range(1, n):
    size = 1
    while i < n and nums[i] - nums[i - 1] == 1:
        size += 1
        i += 1
    res = max(res, size)

print(res)

nums = [1, 20, 10, 15, 3, 2]
n = len(nums)

numsSet = set(nums)
for val in numsSet:
    if val - 1 not in numsSet:
        size = 1
        while val + size in numsSet:
            size += 1
        res = max(res, size)

print(res)
