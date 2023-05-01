# T=nlogn,S=n
def v(nums):
    nums = sorted(nums)
    for index in range(len(nums)):
        if index != nums[index]:
            return index
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
    expected = (n * (n + 1)) // 2
    actual = sum(nums)
    return expected - actual


# T=n,S=1
def y(nums):
    n = len(nums)
    res = 0
    for val in nums:
        res ^= val
    for i in range(n + 1):
        res ^= i
    return res


# T=n,S=1
def z(nums):
    n = len(nums)
    presentIndex = 0
    while presentIndex < n:
        correctIndex = nums[presentIndex]
        if -1 < correctIndex < n and nums[presentIndex] != nums[correctIndex]:
            nums[correctIndex], nums[presentIndex] = nums[presentIndex], nums[correctIndex]
        else:
            presentIndex += 1
    for presentIndex in range(n):
        if presentIndex != nums[presentIndex]:
            return presentIndex
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
    print(z(nums), nums)
