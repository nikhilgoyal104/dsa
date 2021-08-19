def reverse(nums, i):
    low, high = i, len(nums) - 1
    while low < high:
        nums[low], nums[high] = nums[high], nums[low]
        low, high = low + 1, high - 1


# T=nk,S=1
def x(n, k):
    nums = list(range(1, n + 1))
    for _ in range(k - 1):
        i = n - 1
        while i > 0 and nums[i - 1] >= nums[i]:
            i -= 1
        j = i
        while j < n and nums[j] > nums[i - 1]:
            j += 1
        nums[i - 1], nums[j - 1] = nums[j - 1], nums[i - 1]
        reverse(nums, i)
    return ''.join(map(str, nums))


# T=n²,S=n
def y(n, k):
    res, nums = [], list(range(1, n + 1))
    k, fact = k - 1, [1] * n
    for i in range(1, n):
        fact[i] = fact[i - 1] * i
    for i in range(n - 1, -1, -1):
        index, k = divmod(k, fact[i])
        res.append(nums.pop(index))
    return ''.join(map(str, res))


for n, k in [
    (3, 3), (4, 9), (3, 1), (4, 14), (4, 21)
]:
    print(x(n, k), end=' ')
    print(y(n, k))
