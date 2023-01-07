def main(nums):
    n = len(nums)

    def dfs(start, prev):
        print(nums[prev] if prev != -1 else None, end=' ')
        for i in range(start, n):
            dfs(i + 1, i)

    dfs(0, -1)


for nums in [
    [1, 2, 3],
    [1, 2, 3, 4]
]:
    main(nums)
    print()
