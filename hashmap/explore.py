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
