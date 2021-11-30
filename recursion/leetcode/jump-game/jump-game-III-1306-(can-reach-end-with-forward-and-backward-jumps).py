# T=n,S=n
def main(nums, start):
    n, vis = len(nums), set()

    def dfs(i):
        if i < 0 or i > n - 1 or i in vis:
            return False
        if not nums[i]:
            return True
        vis.add(i)
        return dfs(i + nums[i]) or dfs(i - nums[i])

    return dfs(start)


for nums, start in [
    ([4, 2, 3, 0, 3, 1, 2], 5),
    ([4, 2, 3, 0, 3, 1, 2], 0),
    ([3, 0, 2, 1, 2], 2)
]:
    print(main(nums, start))
