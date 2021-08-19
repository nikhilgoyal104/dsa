def x(nums, tar):
    n = len(nums)

    def dfs(start, sum):
        if sum == tar:
            return [[]]
        if sum > tar:
            return []
        res = []
        for i in range(start, n):
            for path in dfs(i + 1, sum + nums[i]):
                res.append([nums[i]] + path)
        return res

    return dfs(0, 0)


# T=2ⁿ,S=n
def y(nums, tar):
    n = len(nums)

    def dfs(i, sum, path):
        if sum == tar:
            return [path]
        if sum > tar or i == n:
            return []
        inc = dfs(i + 1, sum + nums[i], path + [nums[i]])
        exc = dfs(i + 1, sum, path)
        return inc + exc

    return dfs(0, 0, [])


def z(nums, tar):
    n = len(nums)

    def dfs(i, sum):
        if sum == tar:
            return [[]]
        if sum > tar or i == n:
            return []
        res = []
        inc = dfs(i + 1, sum + nums[i])
        for path in inc:
            res.append([nums[i]] + path)
        exc = dfs(i + 1, sum)
        return res + exc

    return dfs(0, 0)


for nums, tar in [
    ([1, 2, 3], 5),
    ([2, 5, 1, 3, 4], 7),
    ([1, 2, 3, 8, 7, 4], 10),
    ([1, 2, 3], 6),
    ([7, 3, 5], 8)
]:
    print(x(nums, tar))
    print(y(nums, tar))
    print(z(nums, tar))
