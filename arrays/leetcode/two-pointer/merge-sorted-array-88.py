# T=m+n,S=m
def main(nums1, nums2, m, n):
    acopy = nums1[:m]
    i = j = k = 0
    while i < m and j < n:
        if acopy[i] < nums2[j]:
            nums1[k] = acopy[i]
            i += 1
        else:
            nums1[k] = nums2[j]
            j += 1
        k += 1
    while i < m:
        nums1[k] = acopy[i]
        i += 1
        k += 1
    while j < n:
        nums1[k] = nums2[j]
        j += 1
        k += 1
    print(nums1)


for nums1, nums2, m, n in [
    ([1, 2, 3, 0, 0, 0], [2, 5, 6], 3, 3),
    ([4, 5, 6, 0, 0, 0], [1, 2, 3], 3, 3),
    ([0], [1], 0, 1)
]:
    main(nums1, nums2, m, n)

print()


# T=m+n,S=1
def main(nums1, nums2, m, n):
    i, j, k = m - 1, n - 1, m + n - 1
    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1
    while i >= 0:
        nums1[k] = nums1[i]
        i -= 1
        k -= 1
    while j >= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1
    print(nums1)


for nums1, nums2, m, n in [
    ([1, 2, 3, 0, 0, 0], [2, 5, 6], 3, 3),
    ([4, 5, 6, 0, 0, 0], [1, 2, 3], 3, 3),
    ([0], [1], 0, 1)
]:
    main(nums1, nums2, m, n)
