# T=n
def x(nums):
    def dfs(nums):
        if not nums:
            return []
        if type(nums[0]) is list:
            return dfs(nums[0]) + dfs(nums[1:])
        return [nums[0]] + dfs(nums[1:])

    return dfs(nums)


# T=n
def y(nums):
    def dfs(nums):
        res = []
        for val in nums:
            if type(val) is list:
                res += dfs(val)
                continue
            res.append(val)
        return res

    return dfs(nums)


for nums in [
    [],
    [1, 2, 3, 4, 5],
    [[1, 2], [3], [4]],
    [[1, 1], 2, [1, 1]],
    [1, 2, [3, 4, [5, 6]], 7, 8, [9, [10]]]
]:
    print(x(nums))
    print(y(nums))
