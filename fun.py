from math import log2, inf
from heapq import *

s = '2'
print(int(s[:2]))

x = 5

y, x = x, 10
print(x, y)

s = 'applepenapple'

print(s.startswith('apple'))
word = 'apple'
print(s[:len(word)] == 'apple')

print('cat'.startswith('catsdogcats'))

blocked = [[1, 2], [3, 4], [5, 6]]
print([3, 4] in blocked)

blocked = set(map(tuple, blocked))
print(blocked)

count = 1

print(count < 2 or count > 3)

print(int(4 in [1, 23]))

print(int(True))
print(int(False))

nums = [1, 2, 3, 4]
b = [5, 6]

for i, j in zip(nums, b):
    print(i, j)


def foo():
    print('foo')

    def bar():
        print('bar')

    def baz():
        print('baz')

    bar()
    baz()


foo()

print()
decoder, char = {}, 'a'
for i in range(1, 27):
    decoder[str(i)] = char
    char = chr(ord(char) + 1)

grid = [
    [0, 6, 0],
    [5, 8, 7],
    [0, 9, 0]
]

m, n = len(grid), len(grid[0])
x = [val for row in grid for val in row]
print(x)

print(int(log2(pow(10, 9))) + 1)

print(int('01', 2))

num = 12
bits = []
while num:
    bits.append(num & 1)
    num >>= 1

print(bits)

print(1 + (4 == 4))

print(4 == 4)

print(4 + True)

k = 3
nums = [1, 4, 7, 5, 21, 43, 5, 6, 91, 1, 31]
heap = []
for val in nums:
    heappush(heap, val)
    if len(heap) > k:
        heappop(heap)

print(heap)

for val in heap:
    print(val, end=' ')

print()

while heap:
    print(heappop(heap), end=' ')
