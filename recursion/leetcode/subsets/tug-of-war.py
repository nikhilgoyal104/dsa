from math import inf


def main(nums):
    res, n = [inf, None, None], len(nums)
    path1, path2 = [], []

    def dfs(i, sum1, sum2):
        nonlocal res
        if i == n:
            diff = abs(sum1 - sum2)
            if diff < res[0]:
                res[0], res[1], res[2] = diff, path1[:], path2[:]
            return
        if len(path1) < (n + 1) // 2:
            path1.append(nums[i])
            dfs(i + 1, sum1 + nums[i], sum2)
            path1.pop()
        if len(path2) < (n + 1) // 2:
            path2.append(nums[i])
            dfs(i + 1, sum1, sum2 + nums[i])
            path2.pop()

    dfs(0, 0, 0)
    return res


for nums in [
    [1, 2, 3, 4, 5, 6],
    [1, 2, 3, 4, 5],
]:
    print(main(nums))
