# S=n
def x(nums, k):
    if sum(nums) % k != 0:
        return False
    n, total, vis = len(nums), sum(nums) // k, set()

    def dfs(start, sum, k):
        if k == 1:
            return True
        if sum == total:
            return dfs(0, 0, k - 1)
        if sum > total:
            return False
        for i in range(start, n):
            if i in vis:
                continue
            vis.add(i)
            if dfs(i + 1, sum + nums[i], k):
                return True
            vis.remove(i)
        return False

    return dfs(0, 0, k)


for nums, k in [
    ([1, 1, 1, 1, 2, 2, 2, 2], 2),
    ([4, 3, 2, 3, 5, 2, 1], 4),
    ([1, 2, 3, 4], 3),
]:
    print(x(nums, k))
