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
    freq = {}
    for val in nums:
        if val in freq:
            return val
        freq[val] = freq.get(val, 0) + 1


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
        slow, fast = nums[slow], nums[nums[fast]]
        if slow == fast:
            break
    slow = nums[0]
    while slow != fast:
        slow, fast = nums[slow], nums[fast]
    return slow


# T=n,S=1
def z(nums):
    n = len(nums)
    for i in range(n):
        dest = nums[i] - 1
        while nums[i] != nums[dest]:
            nums[i], nums[dest] = nums[dest], nums[i]
            dest = nums[i] - 1
    return nums[n - 1]


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
