from collections import Counter


def w(nums):
    freq = Counter(nums)

    def dfs():
        if not sum(freq.values()):
            return [[]]
        res = []
        for val in freq:
            if freq[val]:
                freq[val] -= 1
                for path in dfs():
                    res.append([val] + path)
                freq[val] += 1
        return res

    return dfs()


for nums in [
    [1],
    [1, 1],
    [1, 1, 2],
    [1, 2, 2, 3],
    [1, 1, 2, 3],
    [1, 1, 5]
]:
    print(w(nums))

print()


def x(nums):
    n, nums, vis = len(nums), sorted(nums), set()

    def dfs():
        if len(vis) == n:
            return [[]]
        res = []
        for i in range(n):
            if (i in vis) or (i and i - 1 not in vis and nums[i] == nums[i - 1]):
                continue
            vis.add(i)
            for path in dfs():
                res.append([nums[i]] + path)
            vis.remove(i)
        return res

    return dfs()


def y(nums):
    n, nums, path, res, vis = len(nums), sorted(nums), [], [], set()

    def dfs():
        if len(vis) == n:
            res.append(path[:])
            return
        for i in range(n):
            if (i in vis) or (i and i - 1 not in vis and nums[i] == nums[i - 1]):
                continue
            vis.add(i)
            path.append(nums[i])
            dfs()
            vis.remove(i)
            path.pop()

    dfs()
    return res


for nums in [
    [1],
    [1, 1],
    [1, 1, 2],
    [1, 2, 2, 3],
    [1, 1, 2, 3],
    [1, 1, 5]
]:
    print(x(nums))
    print(y(nums))
