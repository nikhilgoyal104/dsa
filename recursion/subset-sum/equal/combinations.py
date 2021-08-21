def x(nums, total):
    n = len(nums)

    def dfs(start, sum):
        if sum == total:
            return [[]]
        if sum > total:
            return []
        res = []
        for i in range(start, n):
            for path in dfs(i + 1, sum + nums[i]):
                res.append([nums[i]] + path)
        return res

    return dfs(0, 0)


# T=2ⁿ,S=n
def y(nums, total):
    n = len(nums)

    def dfs(i, sum, path):
        if sum == total:
            return [path]
        if sum > total or i == n:
            return []
        inc = dfs(i + 1, sum + nums[i], path + [nums[i]])
        exc = dfs(i + 1, sum, path)
        return inc + exc

    return dfs(0, 0, [])


def z(nums, total):
    n = len(nums)

    def dfs(i, sum):
        if sum == total:
            return [[]]
        if sum > total or i == n:
            return []
        res = []
        inc = dfs(i + 1, sum + nums[i])
        for path in inc:
            res.append([nums[i]] + path)
        exc = dfs(i + 1, sum)
        return res + exc

    return dfs(0, 0)


for nums, total in [
    ([1, 2, 3], 5),
    ([2, 5, 1, 3, 4], 7),
    ([1, 2, 3, 8, 7, 4], 10),
    ([1, 1, 1, 1, 1], 4),
    ([1, 2, 3], 6),
    ([7, 3, 5], 8)
]:
    print(x(nums, total))
    print(y(nums, total))
    print(z(nums, total))
    print()
