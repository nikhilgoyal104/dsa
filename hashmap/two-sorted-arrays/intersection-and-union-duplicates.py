def intersection(nums1, nums2):
    m, n = len(nums1), len(nums2)
    res = []
    i, j = 0, 0
    while i < m and j < n:
        if nums1[i] < nums2[j]:
            i += 1
        elif nums1[i] > nums2[j]:
            j += 1
        else:
            if not res or res[-1] != nums1[i]:
                res.append(nums1[i])
            i += 1
            j += 1
    return res


def union(nums1, nums2):
    m, n = len(nums1), len(nums2)
    res = []
    i, j = 0, 0
    while i < m and j < n:
        if nums1[i] < nums2[j]:
            if not res or res[-1] != nums1[i]:
                res.append(nums1[i])
            i += 1
        elif nums1[i] > nums2[j]:
            if not res or res[-1] != nums2[j]:
                res.append(nums2[j])
            j += 1
        else:
            if not res or res[-1] != nums1[i]:
                res.append(nums1[i])
            i += 1
            j += 1
    while i < m:
        if not res or res[-1] != nums1[i]:
            res.append(nums1[i])
        i += 1
    while j < n:
        if not res or res[-1] != nums2[j]:
            res.append(nums2[j])
        j += 1
    return res


for nums1, nums2 in [
    ([1, 2, 4, 5, 6], [2, 3, 5, 7]),
    ([1, 2, 2, 3, 4], [2, 2, 4, 6, 7, 8]),
    ([1, 2, 3, 4, 5, 5, 5, 5], [6, 7, 8, 9]),
]:
    print(intersection(nums1, nums2), end=' ')
    print(union(nums1, nums2), end=' ')
    print()
