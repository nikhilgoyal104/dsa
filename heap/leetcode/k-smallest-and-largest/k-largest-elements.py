from heapq import *

inputs = [
    ([11, 3, 2, 1, 15, 5, 4, 45, 88, 96, 50, 45], 3),
    ([2, 10, 5, 17, 7, 18, 6, 4], 3)
]


# T=nlogn,S=n
def main(nums, k):
    return sorted(nums, reverse=True)[:k]


for nums, k in inputs:
    print(main(nums, k))

print()


# T=nlogk,S=k
def main(nums, k):
    return nlargest(k, nums)


for nums, k in inputs:
    print(main(nums, k))

print()


# T=nlogk,S=k
def main(nums, k):
    res = []
    heap = []
    for val in nums:
        heappush(heap, val)
        if len(heap) > k:
            heappop(heap)
    while heap:
        res.append(heappop(heap))
    return res


for nums, k in inputs:
    print(main(nums, k))

print()


# T=n+klogn,S=1
def main(nums, k):
    res = []
    for i in range(len(nums)):
        nums[i] = -nums[i]
    heapify(nums)
    while k:
        res.append(-heappop(nums))
        k -= 1
    return res


for nums, k in inputs:
    print(main(nums, k))
