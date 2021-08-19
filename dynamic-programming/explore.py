print(max([[1, 2, 3], [4, 5, 6], [1, 8, 9]]))

s = ''

print(s.count('*') == len(s))

a = []
print([].count(1))

print('i' * 0)

nums = [1, 2, 3, 3, 3, 4, 5, 5, 5, 7, 8, 8, 8, 9, 9]

i, n, res = 0, len(nums), []

while i < n:
    res.append(nums[i])
    while i + 1 < n and nums[i] == nums[i + 1]:
        i += 1
    i += 1

print(res)

print(ord('a'))