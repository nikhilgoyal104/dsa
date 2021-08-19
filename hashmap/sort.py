from collections import Counter
from operator import itemgetter, attrgetter

nums = ('b', 'g', 'a', 'd', 'f', 'c', 'h', 'e')

print(sorted(nums))
print(sorted(nums, reverse=True))

nums = [[1, 2, 3], [1, 2, 4], [1, 4, 1]]

print(sorted(nums, reverse=True))
print()

nums = [[1, 3, 3], [2, 1, 2], [3, 2, 1]]

for i in range(3):
    print(sorted(nums, key=lambda x: x[i]))

nums = [[1, 3, 3], [2, 1, 2], [3, 2, 1]]
for i in range(3):
    print(sorted(nums, key=itemgetter(i)))

print(sorted(['q', 'w', 'e', 'r', 't', 'y']))
print(sorted(('q', 'w', 'e', 'r', 't', 'y')))
print(sorted({'q', 'w', 'e', 'r', 't', 'y'}))
print(sorted('python'))

nums = ['aaaa', 'bbb', 'cc', 'd']
print(sorted(nums, key=len))

nums = ['dddd', 'ccc', 'bb', 'a']
print(sorted(nums))

s = ['aa', 'BB', 'zz', 'CC']
print(sorted(s))
print(sorted(s, key=str.lower))

participants = [
    ('Alison', 50, 18),
    ('Terence', 75, 12),
    ('David', 75, 20),
    ('Jimmy', 90, 22),
    ('John', 45, 12)
]

p = sorted(participants, key=lambda x: (-x[1], x[0]))
print(p)

nums = [1, 2, 3, 4, 3, 3, 3, 6, 7, 1, 1, 9, 3, 2]
hm = Counter(nums)
print(hm)
print(sorted(nums, key=lambda x: -hm[x]))
print(sorted(nums, key=hm.get, reverse=True))
print(sorted(nums, key=nums.count, reverse=True))

nums = [1, 2, 3, 4, 4, 5, 5, 5, 5, 7, 1, 1, 2, 4, 7, 8, 9, 6, 6, 6]
hm = Counter(nums)
print(hm)
print(sorted(nums, key=lambda x: (hm[x], x)))
print(sorted(nums, key=lambda x: (-hm[x], x)))

nums = [1, 5, 6, 3, 2, 9, 7]
print(sorted(nums, key=lambda x: -x))


class Employee:
    def __init__(self, name, department, age):
        self.name = name
        self.department = department
        self.age = age


employees = [Employee('John', 'IT', 28), Employee('Sam', 'Banking', 20), Employee('Joe', 'Finance', 25), ]
print(sorted(employees, key=lambda x: x.age))
print(sorted(employees, key=attrgetter('age')))

print(sorted(employees, key=attrgetter('age', 'name')))

nums = [100, 4, 200, 1, 3, 2]

c = Counter(nums)
print(sorted(c))
for k in sorted(c):
    print(k, c[k])

hm = {2: 56, 1: 2, 5: 12, 4: 24, 6: 18, 3: 323}
print(sorted(hm.items(), key=lambda x: (x[1], x[0])))

hm = {2: 64, 1: 69, 4: 23, 5: 65, 6: 34, 3: 76}
print(hm.items())
print(sorted(hm.keys()))
print(sorted(hm.keys(), key=hm.get))
print(sorted(hm.keys(), key=lambda x: hm[x]))
print(sorted(hm.keys(), key=lambda x: -hm[x]))
