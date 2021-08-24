def overlap(i1, i2):
    return min(i1[1], i2[1]) > max(i1[0], i2[0])


# T=n²
def x(nums):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if overlap(nums[i], nums[j]):
                return False
    return True


# T=nlogn
def y(nums):
    nums.sort()
    for i in range(len(nums) - 1):
        curr, next = nums[i], nums[i + 1]
        if next[0] < curr[1]:
            return False
    return True


for nums in [
    [[0, 30], [5, 10], [15, 20]],
    [[7, 10], [2, 4]]
]:
    print(x(nums), end=' ')
    print(y(nums), end=' ')
    print()
