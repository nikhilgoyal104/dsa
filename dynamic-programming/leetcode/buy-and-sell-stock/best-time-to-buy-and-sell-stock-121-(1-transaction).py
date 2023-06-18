inputs = [
    [7, 1, 5, 3, 6, 4],
    [7, 6, 4, 3, 1]
]


# T=n²,S=1
def main(nums):
    n = len(nums)
    res = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            res = max(res, nums[j] - nums[i])
    return res


for nums in inputs:
    print(main(nums), end=' ')

print()


# T=2ⁿ,S=n
def main(nums):
    n = len(nums)

    def dfs(i, bought, k):
        if i == n or not k:
            return 0
        nothing = dfs(i + 1, bought, k)
        if bought:
            sell = dfs(i + 1, False, k - 1) + nums[i]
            return max(sell, nothing)
        buy = dfs(i + 1, True, k) - nums[i]
        return max(buy, nothing)

    return dfs(0, False, 1)


for nums in inputs:
    print(main(nums), end=' ')

print()


# T=n,S=n
def main(nums):
    n = len(nums)
    cache = {}

    def dfs(i, bought, k):
        if i == n or not k:
            return 0
        key = i, bought, k
        if key in cache:
            return cache[key]
        nothing = dfs(i + 1, bought, k)
        if bought:
            sell = dfs(i + 1, False, k - 1) + nums[i]
            cache[key] = max(sell, nothing)
            return cache[key]
        buy = dfs(i + 1, True, k) - nums[i]
        cache[key] = max(buy, nothing)
        return cache[key]

    return dfs(0, False, 1)


for nums in inputs:
    print(main(nums), end=' ')
