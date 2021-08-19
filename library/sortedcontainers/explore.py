from sortedcontainers import SortedDict, SortedList, SortedSet, SortedKeyList
from operator import neg

sl = SortedList([10, 5, 8, 9, 42])
sl.add(10)

s2 = SortedList()
for val in [3, 6, 1, 3, 8, -2]:
    s2.add(val)

print(s2)

s2 = SortedSet()
for val in [3, 6, 1, 3, 8, -2]:
    s2.add(val)

print(s2)

sd = SortedDict({'c': 3, 'a': 1, 'b': 2})
print(sd)

print(sd.peekitem())

ss = SortedSet('abracadabra')
print(ss)

skl = SortedKeyList([1, 2, 3, 4, 5], key=neg)
print(skl)

sd = SortedDict()
sd['e'] = 5
sd['b'] = 2
print(sd)

sd = SortedDict(neg, enumerate('abc', start=1))
print(sd)

ss = SortedSet()
ss.add('c')
ss.add('b')
ss.add('a')

print(ss)
