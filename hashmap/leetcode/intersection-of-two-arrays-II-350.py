from collections import Counter


# T=m+n,S=min(m,n)
def x(nums1, nums2):
    freq, res = Counter(nums1), []
    for val in nums2:
        if val in freq and freq[val]:
            res.append(val)
            freq[val] -= 1
    return res


# T=m+n,S=min(m,n)
def y(nums1, nums2):
    freq, res = Counter(nums2), []
    for val in nums1:
        if val in freq and freq[val]:
            res.append(val)
            freq[val] -= 1
    return res


def z(nums1, nums2):
    frequency1, frequency2 = map(Counter, (nums1, nums2))
    return list((frequency1 & frequency2).elements())


for nums1, nums2 in [
    ([1, 1, 2, 2, 2, 3, 5], [1, 1, 1, 2, 2, 4, 5]),
    ([4, 9, 5], [9, 4, 9, 8, 4]),
]:
    print(x(nums1, nums2), end=' ')
    print(y(nums1, nums2), end=' ')
    print(z(nums1, nums2), end=' ')
    print()
