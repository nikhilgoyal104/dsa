from collections import deque


def x(nums, total):
    n = len(nums)
    cache = {}

    def dfs(start, sum):
        if sum == total:
            return 0
        if sum > total:
            return float('inf')
        key = start, sum
        if key in cache:
            return cache[key]
        cache[key] = float('inf')
        for i in range(start, n):
            cache[key] = min(cache[key], 1 + dfs(i, sum + nums[i]))
        return cache[key]

    return dfs(0, 0)


def y(nums, total):
    cache = {total: 0}

    def dfs(sum):
        if sum > total:
            return float('inf')
        if sum in cache:
            return cache[sum]
        cache[sum] = float('inf')
        for val in nums:
            cache[sum] = min(cache[sum], 1 + dfs(sum + val))
        return cache[sum]

    return dfs(0)


def z(nums, total):
    queue = deque([(0, 0)])
    while queue:
        sum, count = queue.popleft()
        if sum == total:
            return count
        if sum > total:
            continue
        for val in nums:
            queue.append((sum + val, count + 1))


for nums, total in [
    ([1, 2, 3], 4),
    ([1, 2, 5], 10),
    ([1, 2, 5], 11),
]:
    print('nums-' + str(nums) + ' total-' + str(total) + '->', str(x(nums, total)))
    print('nums-' + str(nums) + ' total-' + str(total) + '->', str(y(nums, total)))
    print('nums-' + str(nums) + ' total-' + str(total) + '->', str(z(nums, total)))

print()


# T=ns,S=ns
def main(nums, total):
    n = len(nums)
    cache = [[float('inf')] * (total + 1) for _ in range(n)]
    for j in range(total + 1):
        quot, rem = divmod(j, nums[0])
        cache[0][j] = quot if not rem else float('inf')
    for i in range(n):
        cache[i][0] = 0
    for i in range(1, n):
        for j in range(1, total + 1):
            cache[i][j] = min(cache[i - 1][j], 1 + (cache[i][j - nums[i]] if j >= nums[i] else float('inf')))
    return cache[-1][-1]


for nums, total in [
    ([1, 2, 3], 4),
    ([1, 2, 5], 10),
    ([1, 2, 5], 11),
    ([2], 3),
    ([1], 0),
    ([1], 1),
    ([3, 7, 405, 436], 8839),
    ([474, 83, 404, 3], 264)
]:
    print('nums-' + str(nums) + ' total-' + str(total) + '->' + str(main(nums, total)))
