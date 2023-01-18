# T=n,S=n
def main(nums, k):
    n = len(nums)
    res = [0] * n
    for i in range(n):
        res[(i + k) % n] = nums[i]
    nums[:] = res


for nums, k in [
    ([1, 2, 3, 4, 5, 6, 7], 3),
    ([-1, -100, 3, 99], 2)
]:
    main(nums, k)
    print(nums)


def reverse(nums, low, high):
    while low < high:
        nums[low], nums[high] = nums[high], nums[low]
        low, high = low + 1, high - 1


# T=n,S=1
def main(nums, k):
    n = len(nums)
    k %= n
    reverse(nums, 0, n - k - 1)
    reverse(nums, n - k, n - 1)
    reverse(nums, 0, n - 1)


for nums, k in [
    ([1, 2, 3, 4, 5, 6, 7], 3),
    ([-1, -100, 3, 99], 2)
]:
    main(nums, k)
    print(nums)
