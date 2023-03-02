# T=nlogn,S=n
def main(nums):
    if not nums:
        return 0
    res = 1
    nums.sort(key=lambda x: x[1])
    firstEnd = nums[0][1]
    for start, end in nums:
        if firstEnd < start:
            firstEnd = end
            res += 1
    return res


for nums in [
    [[10, 16], [2, 8], [1, 6], [7, 12]],
    [[1, 2], [3, 4], [5, 6], [7, 8]],
    [[1, 2], [2, 3], [3, 4], [4, 5]]
]:
    print(main(nums))
