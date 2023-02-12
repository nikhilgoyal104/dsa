def merge(nums1, nums2):
    res = []
    m, n = len(nums1), len(nums2)
    i = j = 0
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


# T=nlogn,S=n
def main(nums):
    def dfs(low, high):
        if low == high:
            return [nums[low]]
        mid = low + (high - low) // 2
        left = dfs(low, mid)
        right = dfs(mid + 1, high)
        return merge(left, right)

    return dfs(0, len(nums) - 1)


for nums in [
    [7, 4, 1, 3, 6, 8, 2, 5],
    [5, 6, 1, 3, 2, 9],
    [5, 9, 8, 2, 1],
    [5, 9, 3, 1],
    [5, 4, 3, 2, 1],
    [1, 2, 3, 4, 5]
]:
    print(main(nums))
