# T=n,S=1
def main(nums):
    zeros = ones = twos = 0
    for val in nums:
        if val == 0:
            zeros += 1
        elif val == 1:
            ones += 1
        else:
            twos += 1
    for i in range(zeros):
        nums[i] = 0
    for i in range(ones):
        nums[zeros + i] = 1
    for i in range(twos):
        nums[zeros + ones + i] = 2


for nums in [
    [2, 0, 2, 1, 1, 0],
    [2, 0, 1],
    [0],
    [1]
]:
    main(nums)
    print(nums)


# T=n,S=1
def main(nums):
    zeros = ones = twos = 0
    for val in nums:
        if val == 0:
            zeros += 1
        elif val == 1:
            ones += 1
        else:
            twos += 1
    for i in range(len(nums)):
        if i < zeros:
            nums[i] = 0
        elif i < zeros + ones:
            nums[i] = 1
        else:
            nums[i] = 2


for nums in [
    [2, 0, 2, 1, 1, 0],
    [2, 0, 1],
    [0],
    [1]
]:
    main(nums)
    print(nums)


# T=n,S=1
def main(nums):
    def swap(i, j):
        nums[i], nums[j] = nums[j], nums[i]

    beg, mid, end = 0, 0, len(nums) - 1
    while mid <= end:
        if nums[mid] == 0:
            swap(beg, mid)
            mid += 1
            beg += 1
        elif nums[mid] == 2:
            swap(end, mid)
            end -= 1
        else:
            mid += 1


for nums in [
    [2, 0, 2, 1, 1, 0],
    [2, 0, 1],
    [0],
    [1]
]:
    main(nums)
    print(nums)
