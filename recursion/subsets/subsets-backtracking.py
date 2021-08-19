# S=n²
def v(nums):
    n = len(nums)

    def dfs(i, path):
        if i == n:
            return [path]
        inc = dfs(i + 1, path + [nums[i]])
        exc = dfs(i + 1, path)
        return inc + exc

    return dfs(0, [])


# S=n
def w(nums):
    n, path, res = len(nums), [], []

    def dfs(i):
        if i == n:
            res.append(path[:])
            return
        path.append(nums[i])
        dfs(i + 1)
        path.pop()
        dfs(i + 1)

    dfs(0)
    return res


# S=n
def x(nums):
    n, res = len(nums), []

    def dfs(i, path):
        if i == n:
            res.append(path)
            return
        dfs(i + 1, path + [nums[i]])
        dfs(i + 1, path)

    dfs(0, [])
    return res


# S=n²
def y(nums):
    n, res = len(nums), []

    def dfs(start, path):
        res.append(path)
        for i in range(start, n):
            dfs(i + 1, path + [nums[i]])

    dfs(0, [])
    return res


# S=n
def z(nums):
    n, path, res = len(nums), [], []

    def dfs(start):
        res.append(path[:])
        for i in range(start, n):
            path.append(nums[i])
            dfs(i + 1)
            path.pop()

    dfs(0)
    return res


for nums in [
    [1, 2, 3]
]:
    print(v(nums))
    print(w(nums))
    print(x(nums))
    print(y(nums))
    print(z(nums))
