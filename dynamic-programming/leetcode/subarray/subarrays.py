# T=n³
def x(nums):
    res, n = [], len(nums)
    for i in range(n):
        for j in range(i, n):
            res.append(nums[i:j + 1])
    return res


for nums in [
    [], [1], [1, 2, 3]
]:
    print(x(nums))

print()


# T=n³
def x(s):
    res, n = [], len(s)
    for i in range(n):
        for j in range(i, n):
            res.append(s[i:j + 1])
    return res


for s in [
    '', 'a', 'abc'
]:
    print(x(s))
