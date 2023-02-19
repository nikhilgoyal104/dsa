# T=n,S=n
def main(k, nums):
    n = len(nums)
    cache = {}

    def dfs(i, bought, k):
        if i == n or k == 0:
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

    return dfs(0, False, k)


for k, nums in [
    (2, [2, 4, 1]),
    (2, [3, 2, 6, 5, 0, 3])
]:
    print((main(k, nums)))
