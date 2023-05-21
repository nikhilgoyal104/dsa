from heapq import *

inputs = [
    ([3, 2, 1, 5, 6, 4], 2),
    ([3, 2, 3, 1, 2, 4, 5, 5, 6], 4),
    ([7, 4, 6, 3, 9, 1], 3)
]


# T=nlogn,S=n
def main(nums, k):
    return sorted(nums, reverse=True)[-k]


for nums, k in inputs:
    print(main(nums, k), end=' ')

print()


# T=nlogk,S=k
def main(nums, k):
    heap = []
    for val in nums:
        heappush(heap, -val)
        if len(heap) > k:
            heappop(heap)
    return -heap[0]


for nums, k in inputs:
    print(main(nums, k), end=' ')

print()


# T=nlogk,S=k
def main(nums, k):
    return nsmallest(k, nums)[-1]


for nums, k in inputs:
    print(main(nums, k), end=' ')

print()


# T=n+klogn,S=1
def main(nums, k):
    heapify(nums)
    while k > 1:
        heappop(nums)
        k -= 1
    return nums[0]


for nums, k in inputs:
    print(main(nums, k), end=' ')
