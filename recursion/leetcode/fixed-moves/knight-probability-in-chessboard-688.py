# T=8ᵏ,S=k
def x(n, moves, sri, sci):
    offsets = (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)

    def dfs(ri, ci, moves):
        if ri < 0 or ci < 0 or ri > n - 1 or ci > n - 1:
            return 0
        if not moves:
            return 1
        prob = 0
        for i, j in offsets:
            prob += dfs(ri + i, ci + j, moves - 1) / 8
        return prob

    return dfs(sri, sci, moves)


# T=n²k,S=n²k
def y(n, moves, sri, sci):
    dp = {}
    offsets = (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)

    def dfs(ri, ci, moves):
        if ri < 0 or ci < 0 or ri > n - 1 or ci > n - 1:
            return 0
        if not moves:
            return 1
        key = ri, ci, moves
        if key in dp:
            return dp[key]
        dp[key] = 0
        for i, j in offsets:
            dp[key] += dfs(ri + i, ci + j, moves - 1) / 8
        return dp[key]

    return dfs(sri, sci, moves)


for n, moves, sri, sci in [
    (3, 2, 0, 0), (1, 0, 0, 0), (5, 2, 2, 2)
]:
    print(x(n, moves, sri, sci), end=' ')
    print(y(n, moves, sri, sci))
