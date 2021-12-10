def merge(nums1, nums2):
    res = []
    m, n = len(nums1), len(nums2)
    i = j = count = 0
    while i < m and j < n:
        if nums1[i] < nums2[j]:
            res.append(nums1[i])
            i += 1
        else:
            count += (m - i)
            res.append(nums2[j])
            j += 1
    while i < m:
        res.append(nums1[i])
        i += 1
    while j < n:
        res.append(nums2[j])
        j += 1
    return res, count


# T=nlogn,S=n
def main(nums):
    def dfs(low, high):
        if low == high:
            return [nums[low]], 0
        mid = low + (high - low) // 2
        left, leftCount = dfs(low, mid)
        right, rightCount = dfs(mid + 1, high)
        merged, mergedCount = merge(left, right)
        return merged, leftCount + rightCount + mergedCount

    return dfs(0, len(nums) - 1)


for nums in [
    [8, 5, 3, 4, 1, 6, 2],
    [1, 20, 6, 4, 5],
    [2, 4, 1, 3, 5]
]:
    print(main(nums))
