from math import inf


# T=n²
def x(nums):
    n = len(nums)
    least = inf
    for i in range(n - 1):
        for j in range(i + 1, n):
            least = min(least, abs(nums[j] - nums[i]))
    return least


# T=nlogn
def y(nums):
    nums.sort()
    n = len(nums)
    return min(abs(nums[i + 1] - nums[i]) for i in range(n - 1))


for nums in [
    [1, 5, 3, 19, 18, 25],
    [30, 5, 20, 9],
    [1, 19, -4, 31, 38, 25, 100]
]:
    print(x(nums), end=' ')
    print(y(nums))
