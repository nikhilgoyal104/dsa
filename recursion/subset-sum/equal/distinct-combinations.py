def w(nums, total):
    n, nums, path = len(nums), sorted(nums), []

    def dfs(start, sum):
        if sum == total:
            return [path[:]]
        if sum > total:
            return []
        res = []
        for i in range(start, n):
            if i != start and nums[i] == nums[i - 1]:
                continue
            path.append(nums[i])
            res += dfs(i + 1, sum + nums[i])
            path.pop()
        return res

    return dfs(0, 0)


def x(nums, total):
    n, nums = len(nums), sorted(nums)

    def dfs(start, sum, path):
        if sum == total:
            return [path]
        if sum > total:
            return []
        res = []
        for i in range(start, n):
            if i != start and nums[i] == nums[i - 1]:
                continue
            res += dfs(i + 1, sum + nums[i], path + [nums[i]])
        return res

    return dfs(0, 0, [])


def y(nums, total):
    n = len(nums)

    def dfs(i, sum, path):
        if sum == total:
            return [path]
        if sum > total or i == n:
            return []
        inc = dfs(i + 1, sum + nums[i], path + [nums[i]])
        while i < n - 1 and nums[i] == nums[i + 1]:
            i += 1
        exc = dfs(i + 1, sum, path)
        return inc + exc

    return dfs(0, 0, [])


def z(nums, total):
    n = len(nums)

    def dfs(i, sum, path):
        if sum == total:
            return [path[:]]
        if sum > total or i == n:
            return []
        path.append(nums[i])
        inc = dfs(i + 1, sum + nums[i], path)
        path.pop()
        while i < n - 1 and nums[i] == nums[i + 1]:
            i += 1
        exc = dfs(i + 1, sum, path)
        return inc + exc

    return dfs(0, 0, [])


for nums, total in [
    ([10, 1, 2, 7, 6, 1, 5], 8),
    ([2, 5, 2, 1, 2], 5),
    ([1, 1, 1, 1, 1], 4)

]:
    print(w(nums, total))
    print(x(nums, total))
    print(y(nums, total))
    print(z(nums, total))
    print()
