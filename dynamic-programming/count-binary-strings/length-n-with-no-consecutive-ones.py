def u(n):
    def dfs(i, prev):
        if i == n:
            return 1
        if prev:
            return dfs(i + 1, 0)
        return dfs(i + 1, 0) + dfs(i + 1, 1)

    return dfs(0, 0)


def v(n):
    dp = {}

    def dfs(i, prev):
        if i == n:
            return 1
        key = i, prev
        if key in dp:
            return dp[key]
        dp[key] = dfs(i + 1, 0)
        if not prev:
            dp[key] += dfs(i + 1, 1)
        return dp[key]

    return dfs(0, 0)


def w(n):
    def dfs(i, prev):
        if i == n:
            return 1
        count = 0
        for digit in [0, 1]:
            if prev and digit:
                continue
            count += dfs(i + 1, digit)
        return count

    return dfs(0, False)


def x(n):
    dp = {}

    def dfs(i, prev):
        if i == n:
            return 1
        key = i, prev
        if key in dp:
            return dp[key]
        dp[key] = 0
        for digit in [0, 1]:
            if prev and digit:
                continue
            dp[key] += dfs(i + 1, digit)
        return dp[key]

    return dfs(0, 0)


def y(n):
    zero, one = [0] * n, [0] * n
    zero[0] = one[0] = 1
    for i in range(1, n):
        zero[i] = zero[i - 1] + one[i - 1]
        one[i] = zero[i - 1]
    return one[-1] + zero[-1]


def z(n):
    zero, one = 1, 1
    for i in range(1, n):
        nzero, none = zero + one, zero
        zero, one = nzero, none
    return one + zero


for n in [1, 2, 3, 4, 5, 30]:
    print(u(n), end=' ')
    print(v(n), end=' ')
    print(w(n), end=' ')
    print(x(n), end=' ')
    print(y(n), end=' ')
    print(z(n))
