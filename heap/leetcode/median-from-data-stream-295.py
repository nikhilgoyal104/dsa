from heapq import *

minhp, maxhp = [], []


def add(val):
    heappush(maxhp, -val)
    heappush(minhp, -heappop(maxhp))
    if len(maxhp) < len(minhp):
        heappush(maxhp, -heappop(minhp))


def peek():
    if len(maxhp) > len(minhp):
        return -maxhp[0]
    return (minhp[0] + -maxhp[0]) / 2


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
