def x(nums):
    n = len(nums)
    res = []
    for i in range(2 ** n):
        val = []
        for j in range(n):
            if i & (1 << j):
                val.append(nums[j])
        res.append(val)
    return res


def y(nums):
    n = len(nums)
    res = []
    for i in range(2 ** n):
        num = i
        val = []
        for j in range(n):
            rem = num % 2
            num //= 2
            if rem:
                val.append(nums[j])
        res.append(val)
    return res


for nums in [
    [1, 2, 3]
]:
    print(str(nums) + '->' + str(x(nums)))
    print(str(nums) + '->' + str(y(nums)))
