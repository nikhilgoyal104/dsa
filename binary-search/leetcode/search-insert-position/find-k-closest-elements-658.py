from heapq import *


# T=nlogn,S=k
def p(nums, k, x):
    nums.sort(key=lambda val: abs(val - x))
    return sorted(nums[:k])


for nums, k, x in [
    ([1, 2, 3, 4, 5], 4, 3),
    ([1, 2, 3, 4, 5], 4, -1),
    ([2, 3, 7, 8, 9], 3, 7),
    ([10, 20, 30, 40, 50, 59], 3, 45),
    ([10, 12, 15, 17, 18, 20, 25], 3, 16)
]:
    print(p(nums, k, x))

print()


# T=nlogk,S=k
def q(nums, k, x):
    heap = []
    for val in nums:
        heappush(heap, (-abs(val - x), -val))
        if len(heap) > k:
            heappop(heap)
    return sorted(-val for _, val in heap)


def index(nums, tar):
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if tar == nums[mid]:
            return mid
        elif tar > nums[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return low


# T=logn+k,S=k
def r(nums, k, x):
    n, pos = len(nums), index(nums, x)
    low, high = pos - 1, pos
    while low > -1 and high < n and k:
        if abs(nums[high] - x) < abs(nums[low] - x):
            high += 1
        else:
            low -= 1
        k -= 1
    while low > -1 and k:
        low -= 1
        k -= 1
    while high < n and k:
        high += 1
        k -= 1
    return nums[low + 1:high]


for nums, k, x in [
    ([1, 2, 3, 4, 5], 4, 3),
    ([1, 2, 3, 4, 5], 4, -1),
    ([2, 3, 7, 8, 9], 3, 7),
    ([10, 20, 30, 40, 50, 59], 3, 45),
    ([10, 12, 15, 17, 18, 20, 25], 3, 16)
]:
    print(q(nums, k, x), end=' ')
    print(r(nums, k, x))
