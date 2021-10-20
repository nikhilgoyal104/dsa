from heapq import *


# T=nlogn,S=1
def main(nums, k):
    print(sorted(nums, reverse=True)[:k])


for nums, k in [
    ([11, 3, 2, 1, 15, 5, 4, 45, 88, 96, 50, 45], 3),
    ([2, 10, 5, 17, 7, 18, 6, 4], 3)
]:
    main(nums, k)

print()


# T=nlogk,S=k
def main(nums, k):
    print(nlargest(k, nums))


for nums, k in [
    ([11, 3, 2, 1, 15, 5, 4, 45, 88, 96, 50, 45], 3),
    ([2, 10, 5, 17, 7, 18, 6, 4], 3)
]:
    main(nums, k)

print()


# T=nlogk,S=k
def main(nums, k):
    heap = []
    for val in nums:
        heappush(heap, val)
        if len(heap) > k:
            heappop(heap)
    while heap:
        print(heappop(heap), end=' ')


for nums, k in [
    ([11, 3, 2, 1, 15, 5, 4, 45, 88, 96, 50, 45], 3),
    ([2, 10, 5, 17, 7, 18, 6, 4], 3)
]:
    main(nums, k)
    print()
