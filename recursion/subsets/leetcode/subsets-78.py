# T=n2ⁿ
def main(nums):
    n, res, path = len(nums), [], []

    def dfs(start):
        res.append(path[:])
        for i in range(start, n):
            path.append(nums[i])
            dfs(i + 1)
            path.pop()

    dfs(0)
    return res


for nums in [
    [],
    [1],
    [1, 2, 3]
]:
    print(main(nums))
