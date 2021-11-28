# T=logn,S=1
def main(nums, target):
    n = len(nums)
    low, high = 0, n - 1
    while low <= high:
        mid = low + (high - low) // 2
        if target >= nums[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return nums[low % n]


for nums, target in [
    (['c', 'f', 'j'], 'a'),
    (['c', 'f', 'j'], 'c'),
    (['c', 'f', 'j'], 'd'),
    (['c', 'f', 'j'], 'g'),
    (['c', 'f', 'j'], 'j'),
    (['c', 'f', 'j'], 'k'),
    (['e', 'e', 'e', 'e', 'e', 'e', 'n', 'n', 'n', 'n'], 'e')
]:
    print(main(nums, target), end=' ')
