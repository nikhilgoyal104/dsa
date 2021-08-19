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
