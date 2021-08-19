from binarytree import build as b


# T=n,S=n
def x(root):
    dp = {None: 0}

    def dfs(root):
        if root in dp:
            return dp[root]
        inc, exc = root.val, 0
        for nbr in [root.left, root.right]:
            inc += dfs(nbr.left) + dfs(nbr.right) if nbr else 0
            exc += dfs(nbr)
        dp[root] = max(inc, exc)
        return dp[root]

    return dfs(root)


for root in [
    b([3, 2, 3, None, 3, None, 1]),
    b([3, 4, 5, 1, 3, None, 1])
]:
    print(x(root))
