inputs1 = [
    ([1, 2, 3], 4),
    ([1, 2, 5], 11),
]


def main(nums, total):
    def dfs(sum):
        if sum == total:
            return 1
        if sum > total:
            return 0
        res = 0
        for val in nums:
            res += dfs(sum + val)
        return res

    return dfs(0)


for nums, total in inputs1:
    print(main(nums, total), end=' ')

print()


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


for nums, total in inputs1:
    print(main(nums, total), end=' ')

print('\n')

inputs2 = [
    ([1, 2, 3], 4),
    ([2, 3, 5], 7),
]


def main(nums, total):
    def dfs(sum):
        if sum == total:
            return [[]]
        if sum > total:
            return []
        res = []
        for val in nums:
            for path in dfs(sum + val):
                res.append([val] + path)
        return res

    return dfs(0)


for nums, total in inputs2:
    print(main(nums, total))
