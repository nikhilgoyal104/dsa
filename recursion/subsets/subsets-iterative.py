def x(nums):
    res, n = [], len(nums)
    for i in range(pow(2, n)):
        val = []
        for j in range(n):
            if i & (1 << j):
                val.append(nums[j])
        res.append(val)
    return res


def y(nums):
    res, n = [], len(nums)
    for i in range(2 ** n):
        num, val = i, []
        for j in range(n):
            quot, rem = divmod(num, 2)
            if rem:
                val.append(nums[j])
        res.append(val)
    return res


for nums in [
    [1, 2, 3]
]:
    print(x(nums))
    print(y(nums))
