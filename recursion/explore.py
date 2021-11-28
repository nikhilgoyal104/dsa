print(str(1))

print(str(range(1, 10)))

print('a' * (4 // 2))

print(['a'])

map1 = {'a': 'xyz'}

print(map1.get('b'))

a = 'abcd'
b = 'abc'

print(set(a))

print(list(range(1, 4)))

vis = set()
vis.update({(1, 2), (3, 4), (5, 6)})
print(vis)

vis.difference_update({(1, 2), (3, 4), (5, 6)})
print(vis)

print(type([1, 2, 3]) == list)
print(type([1, 2, 3]) is list)

a = iter([1, 4, 7])
print(next(a))
print(next(a))
print(next(a))

s = 'abcd'
for i in range(len(s)):
    prefix, suffix = s[:i + 1], s[i + 1:]
    print(prefix, suffix)

print(''.join([]))
