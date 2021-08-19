def x(nums):
    def dfs(nums):
        if not nums:
            return [[]]
        res, subproblem = [], dfs(nums[1:])
        for val in subproblem:
            res.append([nums[0]] + val)
        res += subproblem
        return res

    return dfs(nums)


def y(nums):
    n = len(nums)

    def dfs(i):
        if i == n:
            return [[]]
        res, subproblem = [], dfs(i + 1)
        for val in subproblem:
            res.append([nums[i]] + val)
        res += subproblem
        return res

    return dfs(0)


# T=2ⁿn,S=2ⁿn
def z(nums):
    res = [[]]
    for val in nums:
        lst = [r + [val] for r in res]
        res += lst
    return res


for nums in [
    [1, 2, 3]
]:
    print(x(nums))
    print(y(nums))
    print(z(nums))
