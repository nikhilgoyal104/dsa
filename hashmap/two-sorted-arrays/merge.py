# T=m+n,S=m+n
def main(nums1, nums2):
    m, n = len(nums1), len(nums2)
    res, i, j = [], 0, 0
    while i < m and j < n:
        if nums1[i] < nums2[j]:
            res.append(nums1[i])
            i += 1
        else:
            res.append(nums2[j])
            j += 1
    while i < m:
        res.append(nums1[i])
        i += 1
    while j < n:
        res.append(nums2[j])
        j += 1
    return res


for (nums1, nums2) in [
    ([2, 5, 12, 18, 20], [7, 9, 11, 15, 25, 28, 30, 35]),
    ([1, 3, 5, 7], [2, 4, 6, 8]),
    ([1, 2, 3], [2, 5, 6]),
    ([4, 5, 6], [1, 2, 3])
]:
    print(main(nums1, nums2))
