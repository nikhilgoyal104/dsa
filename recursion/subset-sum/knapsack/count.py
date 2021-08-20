def x(nums, total):
    n = len(nums)

    def dfs(i, sum):
        if sum > total:
            return 0
        if sum == total or i == n:
            return 1
        inc = dfs(i + 1, sum + nums[i])
        exc = dfs(i + 1, sum)
        return inc + exc

    return dfs(0, 0)


for nums, total in [
    ([1, 2, 3], 5),
    ([2, 5, 1, 3, 4], 7),
    ([1, 2, 3, 8, 7, 4], 10),
    ([1, 2, 3], 6),
    ([7, 3, 5], 8)
]:
    print(x(nums, total))
