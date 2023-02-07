def reverse(nums, i):
    low, high = i, len(nums) - 1
    while low < high:
        nums[low], nums[high] = nums[high], nums[low]
        low, high = low + 1, high - 1


# T=d,S=d
def main(n):
    nums = list(str(n))
    size = len(nums)
    i = size - 1
    while i >= 1 and nums[i - 1] >= nums[i]:
        i -= 1
    if not i:
        return -1
    j = i
    while j < size and nums[j] > nums[i - 1]:
        j += 1
    nums[i - 1], nums[j - 1] = nums[j - 1], nums[i - 1]
    reverse(nums, i)
    res = int(''.join(nums))
    return res if res < pow(2, 31) else -1


for n in [
    233,
    452654,
    45132,
    321,
    12,
    21,
    2147483486
]:
    print(main(n))
