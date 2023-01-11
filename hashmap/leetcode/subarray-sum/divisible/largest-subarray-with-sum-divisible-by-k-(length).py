# T=n,S=k
def main(nums, k):
    res, n = 0, len(nums)
    sum, remainderToIndex = 0, {0: -1}
    for i in range(n):
        sum += nums[i]
        remainder = sum % k
        if remainder in remainderToIndex:
            res = max(res, i - remainderToIndex[remainder])
        if remainder not in remainderToIndex:
            remainderToIndex[remainder] = i
    return res


for nums, k in [
    ([2, 3, 5, 4, 5, 3, 4], 7),
    ([2, 7, 6, 1, 4, 5], 3),
    ([2, -6, 3, 1, 2, 8, 2, 1], 7),
    ([4, 5, 0, -2, -3, 1], 5),
    ([-2, 2, -5, 12, -11, -1, 7], 3),
    ([5], 9)
]:
    print(main(nums, k))
