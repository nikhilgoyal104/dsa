# T=n³
def main(nums):
    n = len(nums)
    res = []
    for i in range(n):
        for j in range(i, n):
            res.append(nums[i:j + 1])
    return res


for nums in [
    [], [1], [1, 2, 3]
]:
    print(main(nums))

print()


# T=n³
def main(s):
    n = len(s)
    res = []
    for i in range(n):
        for j in range(i, n):
            res.append(s[i:j + 1])
    return res


for s in [
    '', 'a', 'abc'
]:
    print(main(s))
