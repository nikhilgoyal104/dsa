# T=4ᵏ,S=k
def x(m, n, sri, sci, moves):
    def dfs(ri, ci, moves):
        if ri in [-1, m] or ci in [-1, n]:
            return 1
        if not moves:
            return 0
        count = 0
        for i, j in (0, 1), (1, 0), (-1, 0), (0, -1):
            count += dfs(ri + i, ci + j, moves - 1)
        return count

    return dfs(sri, sci, moves) % (pow(10, 9) + 7)


for m, n, moves, sri, sci in [
    (2, 2, 2, 0, 0),
    (1, 3, 3, 0, 1),
]:
    print(x(m, n, sri, sci, moves), end=' ')

print()


# T=mnk,S=mnk
def y(m, n, sri, sci, moves):
    dp = {}

    def dfs(ri, ci, moves):
        if ri in [-1, m] or ci in [-1, n]:
            return 1
        if not moves:
            return 0
        key = ri, ci, moves
        if key in dp:
            return dp[key]
        dp[key] = 0
        for i, j in (0, 1), (1, 0), (-1, 0), (0, -1):
            dp[key] += dfs(ri + i, ci + j, moves - 1)
        return dp[key]

    return dfs(sri, sci, moves) % (pow(10, 9) + 7)


for m, n, moves, sri, sci in [
    (2, 2, 2, 0, 0),
    (1, 3, 3, 0, 1),
    (8, 50, 23, 5, 26)
]:
    print(y(m, n, sri, sci, moves), end=' ')
