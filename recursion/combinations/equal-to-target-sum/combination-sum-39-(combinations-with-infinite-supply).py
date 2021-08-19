def x(nums, tar):
    n, path, res = len(nums), [], []

    def dfs(start, sum):
        if sum == tar:
            res.append(path[:])
            return
        if sum > tar:
            return
        for i in range(start, n):
            path.append(nums[i])
            dfs(i, sum + nums[i])
            path.pop()

    dfs(0, 0)
    return res


def y(nums, tar):
    n = len(nums)

    def dfs(start, sum, path):
        if sum == tar:
            return [path]
        if sum > tar:
            return []
        res = []
        for i in range(start, n):
            res += dfs(i, sum + nums[i], path + [nums[i]])
        return res

    return dfs(0, 0, [])


def z(nums, tar):
    n = len(nums)

    def dfs(i, tar, path):
        if not tar:
            return [path]
        if tar < 0 or i == n:
            return []
        inc = dfs(i, tar - nums[i], path + [nums[i]])
        exc = dfs(i + 1, tar, path)
        return inc + exc

    return dfs(0, tar, [])


for nums, tar in [
    ([2, 5, 1, 3, 4], 7),
    ([2, 3, 6, 7], 7),
    ([2, 3, 5], 8),
    ([2], 1)
]:
    print(x(nums, tar))
    print(y(nums, tar))
    print(z(nums, tar))
