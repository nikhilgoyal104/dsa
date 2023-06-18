def x(nums, total):
    n = len(nums)

    def dfs(start, sum):
        if sum == total:
            return 1
        if sum > total:
            return 0
        res = 0
        for i in range(start, n):
            res += dfs(i, sum + nums[i])
        return res

    return dfs(0, 0)


def y(nums, total):
    n = len(nums)
    cache = {}

    def dfs(start, sum):
        if sum == total:
            return 1
        if sum > total:
            return 0
        key = start, sum
        if key in cache:
            return cache[key]
        cache[key] = 0
        for i in range(start, n):
            cache[key] += dfs(i, sum + nums[i])
        return cache[key]

    return dfs(0, 0)


# T=ns,S=ns
# cache[i][j] = number of ways of making sum j from numbers till index i
def z(nums, total):
    n = len(nums)
    cache = [[0] * (total + 1) for _ in range(n)]
    for j in range(total + 1):
        cache[0][j] = int(j % nums[0] == 0)
    for i in range(n):
        cache[i][0] = 1
    for i in range(1, n):
        for j in range(1, total + 1):
            cache[i][j] = cache[i - 1][j] + (cache[i][j - nums[i]] if j >= nums[i] else 0)
    return cache[-1][-1]


for nums, total in [
    ([1, 2, 3], 4),
    ([1, 2, 3], 5),
    ([1, 2, 5], 11),
    ([4, 2, 7, 1, 3], 10)
]:
    print('nums-' + str(nums) + ' total-' + str(total) + '->' + str(x(nums, total)))
    print('nums-' + str(nums) + ' total-' + str(total) + '->' + str(y(nums, total)))
    print('nums-' + str(nums) + ' total-' + str(total) + '->' + str(z(nums, total)))

print('\ncombinations\n')


def main(nums, total):
    n = len(nums)

    def dfs(start, sum):
        if sum == total:
            return [[]]
        if sum > total:
            return []
        res = []
        for i in range(start, n):
            for path in dfs(i, sum + nums[i]):
                res.append([nums[i]] + path)
        return res

    return dfs(0, 0)


for nums, total in [
    ([1, 2, 3], 4),
    ([1, 2, 3], 5),
    ([1, 2, 5], 11),
    ([4, 2, 7, 1, 3], 10)
]:
    print('nums-' + str(nums) + ' total-' + str(total) + '->' + str(main(nums, total)))

print('\ncombinations\n')


def main(nums, total):
    n = len(nums)
    cache = {}

    def dfs(start, sum):
        if sum == total:
            return [[]]
        if sum > total:
            return []
        key = start, sum
        if key in cache:
            return cache[key]
        cache[key] = []
        for i in range(start, n):
            for path in dfs(i, sum + nums[i]):
                cache[key].append([nums[i]] + path)
        return cache[key]

    return dfs(0, 0)


for nums, total in [
    ([1, 2, 3], 4),
    ([1, 2, 3], 5),
    ([1, 2, 5], 11),
    ([4, 2, 7, 1, 3], 10)
]:
    print('nums-' + str(nums) + ' total-' + str(total) + '->' + str(main(nums, total)))
