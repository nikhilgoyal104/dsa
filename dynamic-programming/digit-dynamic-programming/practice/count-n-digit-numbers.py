def main(n):
    dp = {n: 1}

    def dfs(i):
        if i in dp:
            return dp[i]
        dp[i] = 0
        for digit in range(10):
            if not i and not digit:
                continue
            dp[i] += dfs(i + 1)
        return dp[i]

    return dfs(0)


for d in [1, 2, 3]:
    print(main(d))
