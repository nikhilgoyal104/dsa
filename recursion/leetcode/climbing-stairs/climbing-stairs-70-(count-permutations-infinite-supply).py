# T=2ⁿ,S=n
def main(n):
    def dfs(target):
        if not target:
            return 1
        if target < 0:
            return 0
        res = 0
        for jump in [1, 2]:
            res += dfs(target - jump)
        return res

    return dfs(n)


for n in [
    2, 3, 6
]:
    print(main(n), end=' ')

print()


# T=n,S=n
def main(n):
    cache = {0: 1}

    def dfs(target):
        if target in cache:
            return cache[target]
        if target < 0:
            return 0
        cache[target] = 0
        for jump in [1, 2]:
            cache[target] += dfs(target - jump)
        return cache[target]

    return dfs(n)


for n in [
    2, 3, 6, 35, 45
]:
    print(main(n), end=' ')


# T=n,S=n
def main(n):
    cache = [0] * (n + 1)
    cache[0] = 1
    for target in range(1, n + 1):
        for coin in [1, 2]:
            if target >= coin:
                cache[target] += cache[target - coin]
    return cache[-1]


for n in [
    2, 3, 6, 35, 45
]:
    print(main(n))
