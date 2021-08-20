def x(nums, total):
    n, vis = len(nums), set()

    def dfs(sum):
        if sum == total:
            return 1
        if sum > total:
            return 0
        res = 0
        for i in range(n):
            if i in vis:
                continue
            vis.add(i)
            res += dfs(sum + nums[i])
            vis.remove(i)
        return res

    return dfs(0)


for nums, total in [
    ([2, 3, 5, 6, 7], 12),
]:
    print(x(nums, total))


def x(nums, total):
    n, vis = len(nums), set()

    def dfs(sum):
        if sum == total:
            return [[]]
        if sum > total:
            return []
        res = []
        for i in range(n):
            if i in vis:
                continue
            vis.add(i)
            for path in dfs(sum + nums[i]):
                res.append([nums[i]] + path)
            vis.remove(i)
        return res

    return dfs(0)


for nums, total in [
    ([2, 3, 5, 6, 7], 12),
]:
    print(x(nums, total))
