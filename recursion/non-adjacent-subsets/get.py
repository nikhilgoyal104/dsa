def x(nums):
    n = len(nums)

    def dfs(i, path):
        if i >= n:
            return [path]
        return dfs(i + 2, path + [nums[i]]) + dfs(i + 1, path)

    return dfs(0, [])


def y(nums):
    n, res = len(nums), []

    def dfs(start, path):
        res.append(path)
        for i in range(start, n):
            dfs(i + 2, path + [nums[i]])

    dfs(0, [])
    return res


for nums in [
    [1, 2, 3]
]:
    print(x(nums))
    print(y(nums))
