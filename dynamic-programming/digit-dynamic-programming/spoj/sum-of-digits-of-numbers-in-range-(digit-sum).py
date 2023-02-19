def x(nums, b):
    def helper(n):
        n, cache = str(n), {}
        size = len(n)

        def dfs(i, restrict, sum):
            if i == size:
                return sum
            key = i, restrict, sum
            if key in cache:
                return cache[key]
            cache[key] = 0
            limit = int(n[i]) if restrict else 9
            for digit in range(limit + 1):
                cache[key] += dfs(i + 1, False if digit < limit else restrict, sum + digit)
            return cache[key]

        return dfs(0, True, 0)

    return helper(high) - helper(low - 1) if low else helper(high)


for low, high in [
    (0, 10),
    (28, 31),
    (1234, 56789)
]:
    print(x(low, high))
