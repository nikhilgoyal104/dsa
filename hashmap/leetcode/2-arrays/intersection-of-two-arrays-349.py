from collections import Counter


# T=m+n,S=m+n
def x(nums1, nums2):
    res = []
    hm = Counter(nums1)
    for val in nums2:
        if val in hm:
            res.append(val)
            del hm[val]
    return res


# T=m+n,S=m+n
def y(nums1, nums2):
    res = []
    nums1Set = set(nums1)
    for val in nums2:
        if val in nums1Set:
            res.append(val)
            nums1Set.remove(val)
    return res


# T=m+n,S=m+n
def z(nums1, nums2):
    return list(set(nums1) & set(nums2))


for nums1, nums2 in [
    ([1, 1, 2, 2, 2, 3, 5], [1, 1, 1, 2, 2, 4, 5]),
    ([4, 9, 5], [9, 4, 9, 8, 4]),
]:
    print(x(nums1, nums2))
    print(y(nums1, nums2))
    print(z(nums1, nums2))
