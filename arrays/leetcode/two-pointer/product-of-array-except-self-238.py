inputs = [
    [1, 2, 3, 0, 5, 6, 0],
    [-1, 1, 0, -3, 3],
    [4, 5, 1, 8, 2],
    [1, 2, 3, 4]
]


# T=n,S=1
def main(nums):
    n = len(nums)
    zeros = zeroIndex = 0
    product = 1
    for i, val in enumerate(nums):
        if val == 0:
            zeros += 1
            zeroIndex = i
            if zeros > 1:
                return [0] * n
        else:
            product *= val
    res = [0] * n
    if zeros == 1:
        res[zeroIndex] = product
        return res
    return [product // val for val in nums]


for nums in inputs:
    print(main(nums))

print()


# T=n,S=n
def main(nums):
    n = len(nums)
    res = [1] * n
    left = [1] * n
    for i in range(1, n):
        left[i] = left[i - 1] * nums[i - 1]
    right = [1] * n
    for i in range(n - 2, -1, -1):
        right[i] = right[i + 1] * nums[i + 1]
    for i in range(n):
        res[i] = left[i] * right[i]
    return res


for nums in inputs:
    print(main(nums))

print()


# T=n,S=1
def main(nums):
    n = len(nums)
    res = [1] * n
    for i in range(1, n):
        res[i] = res[i - 1] * nums[i - 1]
    right = 1
    for i in range(n - 1, -1, -1):
        res[i] *= right
        right *= nums[i]
    return res


for nums in inputs:
    print(main(nums))
