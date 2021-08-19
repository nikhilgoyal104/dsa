def x(nums, tar):
    n = len(nums)

    def dfs(start, sum):
        if sum == tar:
            return [[]]
        if sum > tar:
            return []
        res = []
        for i in range(start, n):
            for path in dfs(i, sum + nums[i]):
                res.append([nums[i]] + path)
        return res

    return dfs(0, 0)


# T=(tar/m)nᵗ/ᵐ,S=tar/m(nᵗ/ᵐ)
def y(nums, tar):
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


for nums, tar in [
    ([2, 3, 6, 7], 7),
    ([2, 3, 5], 8),
    ([2], 1),
]:
    print(x(nums, tar))
    print(y(nums, tar))
