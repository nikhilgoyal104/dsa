from collections import deque


# T=nk,S=n
def p(nums, x, y):
    n = len(nums)

    if nums[n - 1] == '1':
        return False

    def dfs(i, cache):
        if i > n - 1 or nums[i] == '1':
            return False
        if i == n - 1:
            return True
        if i in cache:
            return cache[i]
        cache[i] = False
        for val in range(x, y + 1):
            if dfs(i + val, cache):
                cache[i] = True
                return True
        return False

    return dfs(0, {})


# T=nk,S=n
def q(nums, x, y):
    n = len(nums)
    cache = [False] * n
    cache[0] = True
    for i in range(1, n):
        if nums[i] == '1':
            continue
        for j in range(x, y + 1):
            if i - j > -1 and cache[i - j]:
                cache[i] = True
                break
    return cache[-1]


# T=nk,S=n
def r(nums, x, y):
    n = len(nums)
    cache = [False] * n
    cache[-1] = True
    for i in range(n - 2, -1, -1):
        if nums[i] == '1':
            continue
        for j in range(x, y + 1):
            if i + j < n and cache[i + j]:
                cache[i] = True
                break
    return cache[0]


# T=nk,S=n
def s(nums, x, y):
    n = len(nums)
    queue = deque([0])
    vis = {0}
    while queue:
        i = queue.popleft()
        if i == n - 1:
            return True
        for val in range(x, y + 1):
            if i + val < n and nums[i + val] == '0' and i + val not in vis:
                vis.add(i + val)
                queue.append(i + val)
    return False


# T=n,S=n
def t(nums, x, y):
    n = len(nums)
    queue = deque([0])
    mvi = 0
    while queue:
        i = queue.popleft()
        if i == n - 1:
            return True
        neighbours = range(max(i + x, mvi + 1), min(i + y, n - 1) + 1)
        for nbr in neighbours:
            if nums[nbr] == '0':
                queue.append(nbr)
        mvi = i + y
    return False


for nums, x, y in [
    ('011010', 2, 3),
    ('01101110', 2, 3),
]:
    print(p(nums, x, y), end=' ')
    print(q(nums, x, y), end=' ')
    print(r(nums, x, y), end=' ')
    print(s(nums, x, y), end=' ')
    print(t(nums, x, y))
