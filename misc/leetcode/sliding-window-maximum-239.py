from collections import deque


# T=nk
def x(nums, k):
    n, res = len(nums), []
    for i in range(n - k + 1):
        maxVal = nums[i]
        for j in range(1, k):
            maxVal = max(maxVal, nums[i + j])
        res.append(maxVal)
    return res


# T=n,S=n
def y(nums, k):
    n, queue = len(nums), deque()
    for i in range(k):
        while queue and queue[-1][1] <= nums[i]:
            queue.pop()
        queue.append((i, nums[i]))
    res = [queue[0][1]]
    for i in range(k, n):
        while queue and queue[-1][1] <= nums[i]:
            queue.pop()
        queue.append((i, nums[i]))
        if queue[0][0] == i - k:
            queue.popleft()
        res.append(queue[0][1])
    return res


for nums, k in [
    ([1, 3, -1, -3, 5, 3, 6, 7], 3),
    ([1], 1),
    ([1, -1], 1),
    ([9, 10, 9, -7, -4, -8, 2, -6], 5)
]:
    print(x(nums, k), end=' ')
    print(y(nums, k))
