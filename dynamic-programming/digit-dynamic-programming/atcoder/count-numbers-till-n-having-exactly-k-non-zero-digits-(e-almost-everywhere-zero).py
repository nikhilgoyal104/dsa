def main(n, k):
    n = str(n)
    size = len(n)

    def dfs(i, restrict, nzcount):
        if nzcount > k:
            return 0
        if i == size:
            return nzcount == k
        count, limit = 0, int(n[i]) if restrict else 9
        for digit in range(limit + 1):
            count += dfs(i + 1, False if digit < limit else restrict, nzcount + 1 if digit else nzcount)
        return count

    return dfs(0, True, 0)


for n, k in [
    (100, 1),
    (25, 2),
    (314159, 2)
]:
    print(main(n, k), end=' ')

print()


def main(n, k):
    n, dp = str(n), {}
    size = len(n)

    def dfs(i, restrict, nzcount):
        if nzcount > k:
            return 0
        if i == size:
            return nzcount == k
        key = i, restrict, nzcount
        if key in dp:
            return dp[key]
        dp[key], limit = 0, int(n[i]) if restrict else 9
        for digit in range(limit + 1):
            dp[key] += dfs(i + 1, False if digit < limit else restrict, nzcount + 1 if digit else nzcount)
        return dp[key]

    return dfs(0, True, 0)


for n, k in [
    (100, 1),
    (25, 2),
    (314159, 2),
    (9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999, 3)
]:
    print(main(n, k), end=' ')
