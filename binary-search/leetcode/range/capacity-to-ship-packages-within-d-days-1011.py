# T=nlog(sum),S=1
def main(nums, m):
    def count(mid):
        sum, count = 0, 1
        for i in range(len(nums)):
            sum += nums[i]
            if sum > mid:
                sum, count = nums[i], count + 1
        return count

    low, high = max(nums), sum(nums)
    while low <= high:
        mid = low + (high - low) // 2
        if count(mid) <= m:
            high = mid - 1
        else:
            low = mid + 1
    return low


for nums, m in [
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5),
    ([3, 2, 2, 4, 1, 4], 3),
    ([1, 2, 3, 1, 1], 4)
]:
    print(main(nums, m), end=' ')
