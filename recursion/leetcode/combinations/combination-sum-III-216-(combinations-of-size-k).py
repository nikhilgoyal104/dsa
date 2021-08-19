# T=kⁿcₖ,S=kⁿcₖ
def x(k, n):
    tar, nums = n, [i for i in range(1, 10)]

    def dfs(start, sum, k):
        if sum == tar and not k:
            return [[]]
        if sum > tar:
            return []
        res = []
        for i in range(start, 9):
            for path in dfs(i + 1, sum + nums[i], k - 1):
                res.append([nums[i]] + path)
        return res

    return dfs(0, 0, k)


for k, n in [
    (3, 7), (3, 9), (4, 1), (3, 2), (9, 45)
]:
    print(x(k, n))
