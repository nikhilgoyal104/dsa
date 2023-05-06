# T=nlogn,S=n
def main(nums):
    nums.sort()
    res = [nums[0]]
    for i in range(1, len(nums)):
        startTimeOfNextInterval, endTimeOfNextInterval = nums[i]
        endTimeOfCurrentInterval = res[-1][1]
        if startTimeOfNextInterval > endTimeOfCurrentInterval:
            res.append(nums[i])
        else:
            res[-1][1] = max(endTimeOfCurrentInterval, endTimeOfNextInterval)
    return res


for nums in [
    [[1, 3], [2, 6], [8, 10], [15, 18]],
    [[1, 4], [4, 5]],
    [[1, 3], [2, 4], [5, 7], [6, 8]],
    [[1, 4], [2, 3]],
    [[10, 16], [2, 8], [1, 6], [7, 12]],
    [[1, 2], [2, 3], [3, 4], [1, 3]]
]:
    print(main(nums), end='')
    print()
