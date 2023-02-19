# T=ns,S=s
def main(nums, total):
    cache = {total: 1}

    def dfs(sum):
        if sum > total:
            return 0
        if sum in cache:
            return cache[sum]
        cache[sum] = 0
        for val in nums:
            cache[sum] += dfs(sum + val)
        return cache[sum]

    return dfs(0)


for nums, total in [
    ([1, 2, 3], 4),
    ([9], 3)
]:
    print(main(nums, total))
