def main(n):
    cache = {n: 1}

    def dfs(i):
        if i in cache:
            return cache[i]
        cache[i] = 0
        for digit in range(10):
            if not i and not digit:
                continue
            cache[i] += dfs(i + 1)
        return cache[i]

    return dfs(0)


for d in [1, 2, 3]:
    print(main(d))
