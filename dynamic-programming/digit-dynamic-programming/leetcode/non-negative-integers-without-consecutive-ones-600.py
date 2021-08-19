from math import log2


def w(n):
    d = int(log2(n)) + 1

    def dfs(i, prev, num):
        if num > n:
            return 0
        if i == d:
            return 1
        if prev:
            return dfs(i + 1, 0, num)
        return dfs(i + 1, 0, num) + dfs(i + 1, 1, num + 1 * pow(2, d - 1 - i))

    return dfs(0, 0, 0)


def x(n):
    d = int(log2(n)) + 1

    def dfs(i, prev, num):
        if num > n:
            return 0
        if i == d:
            return 1
        count = 0
        for digit in [0, 1]:
            if prev and digit:
                continue
            count += dfs(i + 1, digit, num + digit * pow(2, d - 1 - i))
        return count

    return dfs(0, 0, 0)


def y(n):
    n = bin(n)[2:]
    size = len(n)

    def dfs(i, restrict, prev):
        if i == size:
            return 1
        count, limit = 0, int(n[i]) if restrict else 1
        for digit in range(limit + 1):
            if prev and digit:
                continue
            count += dfs(i + 1, False if digit < limit else restrict, digit)
        return count

    return dfs(0, True, 0)


for n in [10, 88471954, 18492704, 66101402]:
    print(w(n), end=' ')
    print(x(n), end=' ')
    print(y(n))

print()


# T=logn,S=logn
def z(n):
    n, dp = bin(n)[2:], {}
    size = len(n)

    def dfs(i, restrict, prev):
        if i == size:
            return 1
        key = i, restrict, prev
        if key in dp:
            return dp[key]
        dp[key], limit = 0, int(n[i]) if restrict else 1
        for digit in range(limit + 1):
            if prev and digit:
                continue
            dp[key] += dfs(i + 1, False if digit < limit else restrict, digit)
        return dp[key]

    return dfs(0, True, 0)


for n in [10, 88471954, 18492704, 66101402]:
    print(z(n))
