# T=n+k,S=k
def main(nums, k):
    res = []
    n = len(nums)
    presentIndex = 0
    while presentIndex < n:
        correctIndex = nums[presentIndex] - 1
        if -1 < correctIndex < n and nums[presentIndex] != nums[correctIndex]:
            nums[correctIndex], nums[presentIndex] = nums[presentIndex], nums[correctIndex]
        else:
            presentIndex += 1
    extra = set()
    for presentIndex in range(n):
        if len(res) < k and presentIndex != nums[presentIndex] - 1:
            res.append(presentIndex + 1)
            extra.add(nums[presentIndex])
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
