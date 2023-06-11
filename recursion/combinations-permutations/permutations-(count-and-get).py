inputs = [
    ([1, 2, 3], 4),
    ([2, 3, 5, 6, 7], 12),
]


def main(nums, total):
    n = len(nums)
    vis = set()

    def dfs(sum):
        if sum == total:
            return 1
        if sum > total:
            return 0
        res = 0
        for i in range(n):
            if i in vis:
                continue
            vis.add(i)
            res += dfs(sum + nums[i])
            vis.remove(i)
        return res

    return dfs(0)


for nums, total in inputs:
    print('nums-' + str(nums) + ' total-' + str(total) + '->', str(main(nums, total)))

print()


def main(nums, total):
    n = len(nums)
    vis = set()

    def dfs(sum):
        if sum == total:
            return [[]]
        if sum > total:
            return []
        res = []
        for i in range(n):
            if i in vis:
                continue
            vis.add(i)
            for path in dfs(sum + nums[i]):
                res.append([nums[i]] + path)
            vis.remove(i)
        return res

    return dfs(0)


for nums, total in inputs:
    print('nums-' + str(nums) + ' total-' + str(total) + '->', str(main(nums, total)))
