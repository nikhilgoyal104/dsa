from collections import deque
from math import inf


# T=nk
def x(nums, k):
    n, res = len(nums), []
    for i in range(n - k + 1):
        largest = -inf
        for j in range(k):
            largest = max(largest, nums[i + j])
        res.append(largest)
    return res


def push(queue, nums, i):
    while queue and nums[queue[-1]] < nums[i]:
        queue.pop()
    queue.append(i)


# T=n,S=k
def y(nums, k):
    n, queue = len(nums), deque()
    for i in range(k):
        push(queue, nums, i)
    res = [nums[queue[0]]]
    for i in range(k, n):
        push(queue, nums, i)
        if queue[0] == i - k:
            queue.popleft()
        res.append(nums[queue[0]])
    return res


for nums, k in [
    ([1, 3, -1, -3, 5, 3, 6, 7], 3),
    ([1], 1),
    ([1, -1], 1),
    ([9, 10, 9, -7, -4, -8, 2, -6], 5)
]:
    print(x(nums, k), end=' ')
    print(y(nums, k))
