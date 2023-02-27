def main(nums):
    res = 0
    nums.sort(key=lambda x: x[1])
    prevEnd = float('-inf')
    for currStart, currEnd in nums:
        if currStart > prevEnd:
            prevEnd = currEnd
            res += 1
    return res


for nums in [
    [[10, 16], [2, 8], [1, 6], [7, 12]],
    [[1, 2], [3, 4], [5, 6], [7, 8]],
    [[1, 2], [2, 3], [3, 4], [4, 5]]
]:
    print(main(nums))
