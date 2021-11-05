from binarytree import Node as TreeNode


# T=n²,S=n
def main(n):
    dp = {0: 1}

    def dfs(n):
        if n in dp:
            return dp[n]
        dp[n] = 0
        for i in range(n):
            dp[n] += dfs(i) * dfs(n - 1 - i)
        return dp[n]

    return dfs(n)


for n in [
    1, 2, 3, 4, 19
]:
    print(main(n))
