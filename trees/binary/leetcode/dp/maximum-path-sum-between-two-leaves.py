from binarytree import build2


# T=n,S=n
def main(root):
    dp = {None: 0}

    def maxRootToLeafSum(root):
        if not root:
            return 0
        left = maxRootToLeafSum(root.left)
        right = maxRootToLeafSum(root.right)
        dp[root] = root.val + max(left, right)
        return dp[root]

    maxRootToLeafSum(root)

    def dfs(root):
        if not root:
            return 0
        maxLeafToLeafSumLeft = dfs(root.left)
        maxLeafToLeafSumRight = dfs(root.right)
        return max(maxLeafToLeafSumLeft, maxLeafToLeafSumRight, root.val + dp[root.left] + dp[root.right])

    return dfs(root)


for root in [
    build2(
        [-15, 5, 6, -8, 1, 3, 9, 2, 6, None, None, None, None, None, 0, None, None, None, None, 4, -1, None, None, 10]
    )
]:
    print(main(root))


# T=n,S=n
def main(root):
    def dfs(root):
        if not root:
            return 0, 0
        maxLeafToLeafSumLeft, maxRootToLeafSumLeft = dfs(root.left)
        maxLeafToLeafSumRight, maxRootToLeafSumRight = dfs(root.right)
        maxLeafToLeafSum = max(maxLeafToLeafSumLeft, maxLeafToLeafSumRight,
                               root.val + maxRootToLeafSumLeft + maxRootToLeafSumRight)
        maxRootToLeafSum = root.val + max(maxRootToLeafSumLeft, maxRootToLeafSumRight)
        return maxLeafToLeafSum, maxRootToLeafSum

    return dfs(root)[0]


for root in [
    build2(
        [-15, 5, 6, -8, 1, 3, 9, 2, 6, None, None, None, None, None, 0, None, None, None, None, 4, -1, None, None, 10]
    )
]:
    print(main(root))
