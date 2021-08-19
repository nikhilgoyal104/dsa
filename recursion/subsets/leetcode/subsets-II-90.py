def v(nums):
    n, res, nums = len(nums), [], sorted(nums)

    def dfs(start, path):
        res.append(path)
        for i in range(start, n):
            if i != start and nums[i] == nums[i - 1]:
                continue
            dfs(i + 1, path + [nums[i]])

    dfs(0, [])
    return res


def w(nums):
    n, nums = len(nums), sorted(nums)

    def dfs(i, path):
        if i == n:
            return [path]
        inc = dfs(i + 1, path + [nums[i]])
        while i < n - 1 and nums[i] == nums[i + 1]:
            i += 1
        exc = dfs(i + 1, path)
        return inc + exc

    return dfs(0, [])


def x(nums):
    n, nums, res, path = len(nums), sorted(nums), [], []

    def dfs(i):
        if i == n:
            res.append(path[:])
            return
        path.append(nums[i])
        dfs(i + 1)
        path.pop()
        while i < n - 1 and nums[i] == nums[i + 1]:
            i += 1
        dfs(i + 1)

    dfs(0)
    return res


def y(nums):
    res, n, nums = [], len(nums), sorted(nums)

    def dfs(start, path):
        res.append(path)
        for i in range(start, n):
            if i != start and nums[i] == nums[i - 1]:
                continue
            dfs(i + 1, path + [nums[i]])

    dfs(0, [])
    return res


def z(nums):
    n, nums, res, path = len(nums), sorted(nums), [], []

    def dfs(start):
        res.append(path[:])
        for i in range(start, n):
            if i != start and nums[i] == nums[i - 1]:
                continue
            path.append(nums[i])
            dfs(i + 1)
            path.pop()

    dfs(0)
    return res


for nums in [
    [1, 2, 2],
    [4, 4, 4, 1, 4]
]:
    print(v(nums))
    print(w(nums))
    print(x(nums))
    print(y(nums))
    print(z(nums))
    print()
