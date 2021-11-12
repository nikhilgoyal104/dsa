# T=n+k,S=k
def main(nums, k):
    res, n = [], len(nums)
    for i in range(n):
        dest = nums[i] - 1
        while 1 <= nums[i] <= n and nums[i] != nums[dest]:
            nums[i], nums[dest] = nums[dest], nums[i]
            dest = nums[i] - 1
    extra = set()
    for i in range(n):
        if len(res) < k and i != nums[i] - 1:
            res.append(i + 1)
            extra.add(nums[i])
    i = 1
    while len(res) < k:
        if i + n not in extra:
            res.append(i + n)
        i += 1
    return res


for nums, k in [
    ([1, 2, 3, 4], 3),
    ([-2, 11, 1, -3, 2, 8, 4], 4),
    ([-2, 11, 1, -3, 2, 8, 4], 5),
    ([-2, 11, 1, -3, 2, 8, 4], 7),
    ([2, 1, 3, 6, 5], 2)
]:
    print(main(nums, k))
