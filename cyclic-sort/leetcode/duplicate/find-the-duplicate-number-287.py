from collections import Counter


# T=nlogn,S=1
def x(nums):
    nums.sort()
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            return nums[i]


for nums in [
    [1, 3, 4, 2, 2],
    [3, 1, 3, 4, 2],
    [1, 1],
    [1, 1, 2],
    [4, 3, 4, 1, 2],
    [2, 3, 4, 1, 2]
]:
    print(x(nums), end=' ')

print('\n')


# T=n,S=n
def w(nums):
    freq = Counter()
    for val in nums:
        if val in freq:
            return val
        freq[val] += 1


# T=n,S=n
def x(nums):
    vis = set()
    for val in nums:
        if val in vis:
            return val
        vis.add(val)


# T=n,S=1
def y(nums):
    slow = fast = nums[0]
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    return slow


# T=n,S=1
def z(nums):
    n = len(nums)
    presentIndex = 0
    while presentIndex < n:
        correctIndex = nums[presentIndex] - 1
        if -1 < correctIndex < n and nums[presentIndex] != nums[correctIndex]:
            nums[correctIndex], nums[presentIndex] = nums[presentIndex], nums[correctIndex]
        else:
            presentIndex += 1
    return nums[-1]


for nums in [
    [1, 3, 4, 2, 2],
    [3, 1, 3, 4, 2],
    [1, 1],
    [1, 1, 2],
    [4, 3, 4, 1, 2],
    [2, 3, 4, 1, 2]
]:
    print(w(nums), end=' ')
    print(x(nums), end=' ')
    print(y(nums), end=' ')
    print(z(nums))
