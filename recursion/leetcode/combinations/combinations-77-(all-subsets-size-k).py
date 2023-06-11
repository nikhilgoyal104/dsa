def x(n, k):
    nums = [i for i in range(1, n + 1)]

    def dfs(start, size):
        if size == k:
            return [[]]
        res = []
        for i in range(start, n):
            for path in dfs(i + 1, size + 1):
                res.append([nums[i]] + path)
        return res

    return dfs(0, 0)


# T=kⁿcₖ,S=kⁿcₖ
def y(n, k):
    nums = [i for i in range(1, n + 1)]
    res = []
    path = []

    def dfs(start, size):
        if size == k:
            res.append(path[:])
            return
        for i in range(start, n):
            path.append(nums[i])
            dfs(i + 1, size + 1)
            path.pop()

    dfs(0, 0)
    return res


for n, k in [
    (3, 2),
    (4, 2),
    (1, 1)
]:
    print(x(n, k))
    print(y(n, k))
