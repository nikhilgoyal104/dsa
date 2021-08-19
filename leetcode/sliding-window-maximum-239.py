from collections import deque


# T=nk
def x(nums, k):
    n, res = len(nums), []
    for i in range(n - k + 1):
        maximum = nums[i]
        for j in range(1, k):
            maximum = max(maximum, nums[i + j])
        res.append(maximum)
    return res


def order(dq, nums, i):
    while dq and nums[i] > dq[-1][1]:
        dq.pop()
    dq.append((i, nums[i]))


# T=n,S=n
def y(nums, k):
    n = len(nums)
    mi, res = 0, []
    dq = deque([(0, nums[0])])
    for i in range(1, k):
        order(dq, nums, i)
        if nums[i] > nums[mi]:
            mi = i
    res.append(nums[mi])

    for i in range(k, n):
        order(dq, nums, i)
        if dq[0][0] == i - k:
            dq.popleft()
        res.append(dq[0][1])
    return res


for nums, k in [
    ([1, 3, -1, -3, 5, 3, 6, 7], 3),
    ([1], 1),
    ([1, -1], 1),
    ([9, 10, 9, -7, -4, -8, 2, -6], 5)
]:
    print(x(nums, k), end=' ')
    print(y(nums, k))
