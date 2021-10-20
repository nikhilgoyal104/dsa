from math import inf
from collections import deque, defaultdict


# T=kⁿ,S=n
def x(nums):
    n, vis = len(nums), set()

    def dfs(i):
        if i == n - 1:
            return 0
        if i < 0 or i > n - 1 or i in vis:
            return inf
        vis.add(i)
        res = inf
        for val in [i + 1, i - 1] + [j for j in range(n) if nums[i] == nums[j] and i != j]:
            res = min(res, 1 + dfs(val))
        vis.remove(i)
        return res

    return dfs(0)


for nums in [
    [100, -23, -23, 404, 100, 23, 23, 23, 3, 404],
    [7],
    [7, 6, 9, 6, 9, 6, 9, 7],
    [6, 1, 9],
    [11, 22, 7, 7, 7, 7, 7, 7, 7, 22, 13],
    [7, 7, 2, 1, 7, 7, 7, 3, 4, 1],
]:
    print(x(nums), end=' ')

print()


# T=n,S=n
def bfs(nums):
    valToIndexList = defaultdict(list)
    for i, val in enumerate(nums):
        valToIndexList[val].append(i)

    n, vis = len(nums), {0}
    queue = deque([(0, 0)])
    while queue:
        src, dist = queue.popleft()
        if src == n - 1:
            return dist
        for nbr in [src + 1, src - 1] + valToIndexList[nums[src]]:
            if nbr in vis or outside(nbr, n):
                continue
            vis.add(nbr)
            queue.append((nbr, dist + 1))
        valToIndexList[nums[src]] = []


def outside(nbr, n):
    return nbr < 0 or nbr > n - 1


for nums in [
    [100, -23, -23, 404, 100, 23, 23, 23, 3, 404],
    [7],
    [7, 6, 9, 6, 9, 6, 9, 7],
    [6, 1, 9],
    [11, 22, 7, 7, 7, 7, 7, 7, 7, 22, 13],
    [7, 7, 2, 1, 7, 7, 7, 3, 4, 1],
    [68, -94, -44, -18, -1, 18, -87, 29, -6, -87, -27, 37, -57, 7, 18, 68, -59, 29, 7, 53, -27, -59, 18, -1, 18, -18,
     -59, -1, -18, -84, -20, 7, 7, -87, -18, -84, -20, -27],
]:
    print(bfs(nums), end=' ')
