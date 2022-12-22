from collections import Counter, defaultdict

s = 'catsandog'

word = 'cats'
print(s[len(word):])

grid = [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]]

print(list(enumerate(grid)))

hm = Counter()
print(hm[2])
nums = hm[2]
print(nums, hm)
print(hm)
hm[2] += 1
print(hm)

hm = defaultdict(int)
nums = hm[2]
print(hm)

if True or False and False:
    print('yes')

if False or True and True:
    print('yes')

x = 2

if x in [2, 3] and True:
    print('yes')

if x == 2 or x == 3 and True:
    print('yes')

grid = [['.', '.', 'Q', '.'], ['Q', '.', '.', '.'], ['.', '.', '.', 'Q'], ['.', 'Q', '.', '.']]
res = []
config = []
for i, row in enumerate(grid):
    config.append(''.join(row))
res.append(config)
print(config)
print(res)

grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in grid:
    for val in row:
        print(val, end=' ')

print()

print(10 >> 3)

print()
for i in range(4, 5):
    print(i)

print(-1 % 5)


def foo():
    foo = 15
    print(foo)


foo()
