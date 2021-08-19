from heapq import *


def x(nums):
    lst = []
    for start, end in nums:
        lst.append((start, 1))
        lst.append((end, -1))
    lst.sort()
    count, maximum = 0, 0
    for pair in lst:
        count += pair[1]
        maximum = max(maximum, count)
    return maximum


for nums in [
    [[0, 30], [5, 10], [15, 20]],
    [[7, 10], [2, 4]],
    [[1, 10], [2, 7], [3, 19], [8, 12], [10, 20], [11, 30]]
]:
    print(x(nums))
