from math import inf

inputs = [
    ([1, 2], [1, 4, 7]),
    ([], [2, 3]),
    ([5], []),
    ([], [5]),
    ([], [1]),
    ([2], []),
    ([], [1, 2, 3, 4]),
    ([1, 4], [1, 2]),
    ([1, 2, 3], [8, 12]),
    ([1, 2], [3, 4]),
    ([0, 0], [0, 0]),
    ([1, 12, 15, 26, 38], [2, 13, 17, 30, 45]),
    ([1, 2, 3, 6], [4, 6, 8, 10]),
    ([1, 2, 3, 16], [4, 5, 7, 8]),
    ([3, 5, 7, 10, 15], [2, 4, 12]),
    ([3, 9, 12, 13, 14, 19], [7, 17, 20, 24, 26, 28, 30, 32]),
    ([1, 2, 3], [4, 5, 6]),
    ([4, 5, 6], [1, 2, 3]),
    ([1, 2, 3], [4, 5, 6, 7]),
    ([1, 2], [3, 4, 5]),
    ([1, 2, 3], [4, 5]),
    ([4, 5], [1, 2, 3])
]


def median(prev, curr, size):
    return curr if size % 2 else (prev + curr) / 2


# T=m+n,S=1
def main(nums1, nums2):
    m, n = len(nums1), len(nums2)
    prev = curr = None
    mid = (m + n) // 2
    i, j, k = 0, 0, -1
    while i < m and j < n:
        if nums1[i] < nums2[j]:
            prev, curr = curr, nums1[i]
            i += 1
            k += 1
        else:
            prev, curr = curr, nums2[j]
            j += 1
            k += 1
        if k == mid:
            return median(prev, curr, m + n)
    while i < m:
        prev, curr = curr, nums1[i]
        i += 1
        k += 1
        if k == mid:
            return median(prev, curr, m + n)
    while j < n:
        prev, curr = curr, nums2[j]
        j += 1
        k += 1
        if k == mid:
            return median(prev, curr, m + n)


for nums1, nums2 in inputs:
    print(main(nums1, nums2), end=' ')

print()


# T=log(min(m,n)),S=1
def main(nums1, nums2):
    m, n = len(nums1), len(nums2)
    if n < m:
        return main(nums2, nums1)
    low, high = 0, m
    while low <= high:
        nums1LeftCount = low + (high - low) // 2
        nums2LeftCount = (m + n + 1) // 2 - nums1LeftCount
        nums1LeftMax = -inf if nums1LeftCount == 0 else nums1[nums1LeftCount - 1]
        nums1RightMin = inf if nums1LeftCount == m else nums1[nums1LeftCount]
        nums2LeftMax = -inf if nums2LeftCount == 0 else nums2[nums2LeftCount - 1]
        nums2RightMin = inf if nums2LeftCount == n else nums2[nums2LeftCount]
        if nums1LeftMax > nums2RightMin:
            high = nums1LeftCount - 1
        elif nums2LeftMax > nums1RightMin:
            low = nums1LeftCount + 1
        else:
            left_max = max(nums1LeftMax, nums2LeftMax)
            return left_max if (m + n) % 2 else (left_max + min(nums1RightMin, nums2RightMin)) / 2


for nums1, nums2 in inputs:
    print(main(nums1, nums2), end=' ')
