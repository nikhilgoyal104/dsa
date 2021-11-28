from heapq import *

inputs = [
    ([1, 2, 3, 4, 5], 4, 3),
    ([1, 2, 3, 4, 5], 4, -1),
    ([2, 3, 7, 8, 9], 3, 7),
    ([10, 20, 30, 40, 50, 59], 3, 45),
    ([10, 12, 15, 17, 18, 20, 25], 3, 16)
]


# T=nlogn,S=k
def main(nums, k, x):
    nums.sort(key=lambda val: abs(val - x))
    return sorted(nums[:k])


for nums, k, x in inputs:
    print(main(nums, k, x))

print()


# T=nlogk,S=k
def main(nums, k, x):
    heap = []
    for val in nums:
        heappush(heap, (-abs(val - x), -val))
        if len(heap) > k:
            heappop(heap)
    return sorted(-val for _, val in heap)


for nums, k, x in inputs:
    print(main(nums, k, x))

print()


def getPosition(nums, target):
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if target == nums[mid]:
            return mid
        elif target > nums[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return low


# T=logn+k,S=k
def main(nums, k, x):
    n, position = len(nums), getPosition(nums, x)
    low, high = position - 1, position
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


for nums, k, x in inputs:
    print(main(nums, k, x))
