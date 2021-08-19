from heapq import *

minhp, maxhp = [], []


def add(val):
    if maxhp and val > maxhp[0]:
        heappush(maxhp, val)
    else:
        heappush(minhp, -val)
    balance()


def balance():
    n1, n2 = len(minhp), len(maxhp)
    if n1 - n2 == 2:
        heappush(maxhp, -heappop(minhp))
    elif n2 - n1 == 2:
        heappush(minhp, -heappop(maxhp))


def peek():
    n1, n2 = len(minhp), len(maxhp)
    if n1 + n2 == 0:
        return
    if n1 == n2:
        return (-minhp[0] + maxhp[0]) / 2
    elif n1 - n2 == 1:
        return -minhp[0]
    elif n2 - n1 == 1:
        return maxhp[0]


def main(nums):
    global minhp, maxhp
    minhp, maxhp = [], []
    for val in nums:
        add(val)
        print(peek(), end=' ')


for nums in [
    [10, 20, 30, 40],
    [41, 35, 62, 5, 97, 108]
]:
    main(nums)
    print()
