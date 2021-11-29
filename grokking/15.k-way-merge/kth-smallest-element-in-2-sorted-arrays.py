from heapq import *
from math import inf

inputs = [
    ([], [1, 2, 3], 2),
    ([2, 3, 6, 7, 9], [1, 4, 8, 10], 5),
    ([2, 3, 6, 7, 9], [1, 4, 8, 10], 1),
    ([2, 3, 6, 7, 9], [1, 4, 8, 10], 9),
    ([100, 112, 256, 349, 770], [72, 86, 113, 119, 265, 445, 892], 7)
]


# T=k,S=1
def main(nums1, nums2, k):
    m, n = len(nums1), len(nums2)
    i, j = 0, 0
    while i < m and j < n:
        if nums1[i] < nums2[j]:
            if k == 1:
                return nums1[i]
            i += 1
        else:
            if k == 1:
                return nums2[j]
            j += 1
        k -= 1
    while i < m:
        if k == 1:
            return nums1[i]
        i += 1
        k -= 1
    while j < n:
        if k == 1:
            return nums2[j]
        j += 1
        k -= 1
    return -1


for nums1, nums2, k in inputs:
    print(main(nums1, nums2, k), end=' ')

print()


# T=log(min(m,n)),S=1
def main(nums1, nums2, k):
    m, n = len(nums1), len(nums2)
    if n < m:
        return main(nums2, nums1, k)
    low, high = max(0, k - n), min(k, m)
    while low <= high:
        nums1LeftCount = low + (high - low) // 2
        nums2LeftCount = k - nums1LeftCount
        nums1LeftMax = -inf if nums1LeftCount == 0 else nums1[nums1LeftCount - 1]
        nums1RightMin = inf if nums1LeftCount == m else nums1[nums1LeftCount]
        nums2LeftMax = -inf if nums2LeftCount == 0 else nums2[nums2LeftCount - 1]
        nums2RightMin = inf if nums2LeftCount == n else nums2[nums2LeftCount]
        if nums1LeftMax > nums2RightMin:
            high = nums1LeftCount - 1
        elif nums2LeftMax > nums1RightMin:
            low = nums1LeftCount + 1
        else:
            return max(nums1LeftMax, nums2LeftMax)


for nums1, nums2, k in inputs:
    print(main(nums1, nums2, k), end=' ')
