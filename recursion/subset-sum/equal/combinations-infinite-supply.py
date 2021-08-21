def x(nums, total):
    n, path, res = len(nums), [], []

    def dfs(start, sum):
        if sum == total:
            res.append(path[:])
            return
        if sum > total:
            return
        for i in range(start, n):
            path.append(nums[i])
            dfs(i, sum + nums[i])
            path.pop()

    dfs(0, 0)
    return res


def y(nums, total):
    n = len(nums)

    def dfs(start, sum, path):
        if sum == total:
            return [path]
        if sum > total:
            return []
        res = []
        for i in range(start, n):
            res += dfs(i, sum + nums[i], path + [nums[i]])
        return res

    return dfs(0, 0, [])


def z(nums, total):
    n = len(nums)

    def dfs(i, sum, path):
        if sum == total:
            return [path]
        if sum > total or i == n:
            return []
        inc = dfs(i, sum + nums[i], path + [nums[i]])
        exc = dfs(i + 1, sum, path)
        return inc + exc

    return dfs(0, 0, [])


for nums, total in [
    ([2, 5, 1, 3, 4], 7),
    ([2, 3, 6, 7], 7),
    ([2, 3, 5], 8),
    ([2], 1)
]:
    print(x(nums, total))
    print(y(nums, total))
    print(z(nums, total))
    print()
