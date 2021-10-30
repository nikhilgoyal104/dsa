# T=nlogn
def v(nums):
    nums = sorted(nums)
    for val in range(len(nums)):
        if val != nums[val]:
            return val
    return len(nums)


# T=n,S=n
def w(nums):
    aset = set(nums)
    for val in range(len(nums) + 1):
        if val not in aset:
            return val


# T=n,S=1
def x(nums):
    n = len(nums)
    expected, actual = (n * (n + 1)) // 2, sum(nums)
    return expected - actual


# T=n,S=1
def y(nums):
    n, res = len(nums), 0
    for val in nums:
        res ^= val
    for i in range(n + 1):
        res ^= i
    return res


# T=n,S=1
def z(nums):
    n = len(nums)
    for i in range(n):
        dest = nums[i]
        while 0 <= nums[i] <= n - 1 and nums[i] != nums[dest]:
            nums[i], nums[dest] = nums[dest], nums[i]
            dest = nums[i]
    for i in range(n):
        if i != nums[i]:
            return i
    return n


for nums in [
    [1, 2, 3],
    [3, 0, 1],
    [1, 3, 0],
    [0, 1, 2],
    [2, 1, 0],
    [0, 1],
    [9, 6, 4, 2, 3, 5, 7, 0, 1],
    [0]
]:
    print(v(nums), end=' ')
    print(w(nums), end=' ')
    print(x(nums), end=' ')
    print(y(nums), end=' ')
    print(z(nums))
