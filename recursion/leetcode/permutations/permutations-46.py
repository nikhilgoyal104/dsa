def w(nums):
    res, path = [], []

    def dfs(nums):
        if not nums:
            res.append(path[:])
            return
        for i in range(len(nums)):
            path.append(nums[i])
            dfs(nums[:i] + nums[i + 1:])
            path.pop()

    dfs(nums)
    return res


def x(nums):
    n, vis = len(nums), set()

    def dfs():
        if len(vis) == n:
            return [[]]
        res = []
        for i in range(n):
            if i in vis:
                continue
            vis.add(i)
            for path in dfs():
                res.append([nums[i]] + path)
            vis.remove(i)
        return res

    return dfs()


def y(nums):
    n, res, path, vis = len(nums), [], [], set()

    def dfs():
        if len(vis) == n:
            res.append(path[:])
            return
        for i in range(n):
            if i in vis:
                continue
            vis.add(i)
            path.append(nums[i])
            dfs()
            vis.remove(i)
            path.pop()

    dfs()
    return res


def z(nums):
    def dfs(nums):
        if not nums:
            return [[]]
        res = []
        for path in dfs(nums[1:]):
            for i in range(len(path) + 1):
                res.append(path[:i] + [nums[0]] + path[i:])
        return res

    return dfs(nums)


for nums in [
    [1],
    [1, 2, 3],
    [1, 1, 5]
]:
    print(w(nums))
    print(x(nums))
    print(y(nums))
    print(z(nums))
