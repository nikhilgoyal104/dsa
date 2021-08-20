def x(nums, total):
    n = len(nums)

    def dfs(start, sum):
        if sum == total:
            return [[]]
        if sum > total:
            return []
        res = []
        for i in range(start, n):
            for path in dfs(i, sum + nums[i]):
                res.append([nums[i]] + path)
        return res

    return dfs(0, 0)


# T=(total/m)nᵗ/ᵐ,S=total/m(nᵗ/ᵐ)
def y(nums, total):
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


for nums, total in [
    ([2, 3, 6, 7], 7),
    ([2, 3, 5], 8),
    ([2], 1),
]:
    print(x(nums, total))
    print(y(nums, total))
