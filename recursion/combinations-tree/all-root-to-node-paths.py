def main(nums):
    n = len(nums)

    def dfs(start, path):
        print(path, end=' ')
        for i in range(start, n):
            dfs(i + 1, path + [nums[i]])

    dfs(0, [])


for nums in [
    [1, 2, 3],
    [1, 2, 3, 4]
]:
    main(nums)
    print()
