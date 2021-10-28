from math import inf


def main(nums):
    n = len(nums)

    def dfs(i, sum1, sum2):
        if i == n:
            return sum1 * sum2
        return max(dfs(i + 1, sum1 + nums[i], sum2), dfs(i + 1, sum1, sum2 + +nums[i]))

    return dfs(0, 0, 0)


for nums in [
    [1, 2, 3, 4, 5]
]:
    print(main(nums))
