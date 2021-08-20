def x(nums, k):
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


# T=kⁿcₖ,S=kⁿcₖ
def y(nums, k):
    n, path, res = len(nums), [], []

    def dfs(start, count):
        if count == k:
            res.append(path[:])
            return
        for i in range(start, n):
            path.append(nums[i])
            dfs(i + 1, count + 1)
            path.pop()

    dfs(0, 0)
    return res


for nums, k in [
    ([1, 2, 3], 2),
    ([1, 2, 3, 4], 2)
]:
    print(x(nums, k))
    print(y(nums, k))
