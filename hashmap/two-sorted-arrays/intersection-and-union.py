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
            res.append(nums1[i])
            i += 1
        elif nums1[i] > nums2[j]:
            res.append(nums2[j])
            j += 1
        else:
            res.append(nums1[i])
            i += 1
            j += 1
    while i < m:
        res.append(nums1[i])
        i += 1
    while j < n:
        res.append(nums2[j])
        j += 1
    return res


for nums1, nums2 in [
    ([1, 2, 4, 5, 6], [2, 3, 5, 7]),
    ([4, 4, 4, 5, 9], [4, 4, 8, 9, 9])
]:
    print(intersection(nums1, nums2), end=' ')
    print(union(nums1, nums2), end=' ')
    print()
