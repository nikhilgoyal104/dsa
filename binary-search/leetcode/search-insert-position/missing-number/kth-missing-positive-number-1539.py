inputs = [
    ([6, 8, 9, 10], 3),
    ([2, 3, 4, 7, 11], 5),
    ([2, 3, 4, 7, 11], 15),
    ([1, 2, 3, 4], 2),
    ([2, 7, 8, 11, 15], 8),
    ([2, 7, 8, 11, 15], 5),
]


# T=n,S=1
def main(nums, k):
    if k < nums[0]:
        return k
    k -= nums[0] - 1
    for i in range(len(nums) - 1):
        count = nums[i + 1] - nums[i] - 1
        if k <= count:
            return nums[i] + k
        k -= count
    return nums[-1] + k


for nums, k in inputs:
    print(main(nums, k), end=' ')

print()


# T=logn,S=1
def main(nums, k):
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = low + (high - low) // 2
        count = nums[mid] - (mid + 1)
        if k <= count:
            high = mid - 1
        else:
            low = mid + 1
    return k + low


for nums, k in inputs:
    print(main(nums, k), end=' ')
