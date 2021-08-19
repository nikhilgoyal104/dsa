def x(nums):
    n = len(nums)

    def dfs(i):
        if i >= n:
            return 1
        return dfs(i + 2) + dfs(i + 1)

    return dfs(0)


def y(nums):
    n = len(nums)

    def dfs(start):
        count = 1
        for i in range(start, n):
            count += dfs(i + 2)
        return count

    return dfs(0)


for nums in [
    [1, 2, 3]
]:
    print(x(nums))
    print(y(nums))
