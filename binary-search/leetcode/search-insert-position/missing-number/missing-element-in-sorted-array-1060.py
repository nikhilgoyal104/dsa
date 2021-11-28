inputs = [
    ([1, 2, 3], 5),
    ([4, 7, 9, 10], 1),
    ([4, 7, 9, 10], 3),
    ([1, 2, 4], 3)
]


# T=n,S=1
def main(nums, k):
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
        count = nums[mid] - (mid + nums[0])
        if k <= count:
            high = mid - 1
        else:
            low = mid + 1
    return k + high + nums[0]


for nums, k in inputs:
    print(main(nums, k), end=' ')
