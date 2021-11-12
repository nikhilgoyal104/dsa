def main(nums, total):
    n, nums = len(nums), sorted(nums)

    def dfs(start, sum):
        if sum == total:
            return [[]]
        res = []
        for i in range(start, n):
            if i != start and nums[i] == nums[i - 1]:
                continue
            for path in dfs(i + 1, sum + nums[i]):
                res.append([nums[i]] + path)
        return res

    return dfs(0, 0)


for nums, total in [
    ([10, 1, 2, 7, 6, 1, 5], 8),
    ([2, 5, 2, 1, 2], 5)
]:
    print(main(nums, total))
