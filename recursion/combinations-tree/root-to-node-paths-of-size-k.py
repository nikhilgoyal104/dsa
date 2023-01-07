def main(nums, k):
    n = len(nums)

    def dfs(start, count):
        if count == k:
            return [[]]
        res = []
        for i in range(start, n):
            for path in dfs(i + 1, count + 1):
                res.append([nums[i]] + path)
        return res

    return dfs(0, 0)


for nums, k in [
    ([1, 2, 3], 2),
    ([1, 2, 3, 4], 2)
]:
    print(main(nums, k))
