inputs = [
    ([1, 1, 4, 4], 2),
    ([1, 3, 5, 6, 8, 10, 13], 4),
    ([1, 1, 4, 6], 2),
    ([1, 1, 4, 7], 3),
    ([1, 1, 4, 7], 4),
    ([1, 1, 2, 3, 3, 4, 4, 5, 6, 7], 5),
    ([0, 2, 2], 1)
]


# T=log(w)log(n)
def main(nums, k):
    def count(target):
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if target >= nums[mid]:
                low = mid + 1
            else:
                high = mid - 1
        return low

    low, high = nums[0], nums[-1]
    while low <= high:
        mid = low + (high - low) // 2
        if count(mid) >= k:
            high = mid - 1
        else:
            low = mid + 1
    return low


for nums, k in inputs:
    print(main(nums, k), end=' ')

print()


# T=log(w)n
def y(nums, k):
    def count(target):
        i, count = 0, 0
        while i < len(nums) and nums[i] <= target:
            i, count = i + 1, count + 1
        return count

    low, high = nums[0], nums[-1]
    while low <= high:
        mid = low + (high - low) // 2
        if count(mid) >= k:
            high = mid - 1
        else:
            low = mid + 1
    return low


# Let w=max-min
for nums, k in inputs:
    print(main(nums, k), end=' ')
