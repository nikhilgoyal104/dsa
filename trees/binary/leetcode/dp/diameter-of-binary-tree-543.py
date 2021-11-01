from binarytree import build2

inputs = [
    build2([1, 2, 3, 4, 5]),
    build2([1, 2]),
]


# T=n,S=h
def main(root):
    res = 0

    def dfs(root):
        nonlocal res
        if not root:
            return -1
        leftHeight = dfs(root.left)
        rightHeight = dfs(root.right)
        res = max(res, leftHeight + rightHeight + 2)
        return 1 + max(leftHeight, leftHeight)

    dfs(root)
    return res


for root in inputs:
    print(main(root), end=' ')

print()


# T=n,S=n
def main(root):
    dp = {None: -1}

    def height(root):
        if not root:
            return -1
        left = height(root.left)
        right = height(root.right)
        dp[root] = 1 + max(left, right)
        return dp[root]

    def dfs(root):
        if not root:
            return 0
        leftDiameter = dfs(root.left)
        rightDiameter = dfs(root.right)
        return max(leftDiameter, rightDiameter, dp[root.left] + dp[root.right] + 2)

    height(root)
    return dfs(root)


for root in inputs:
    print(main(root), end=' ')

print()


# T=n,S=n
def main(root):
    def dfs(root):
        if not root:
            return 0, -1
        leftDiameter, leftHeight = dfs(root.left)
        rightDiameter, rightHeight = dfs(root.right)
        return max(leftDiameter, rightDiameter, leftHeight + rightHeight + 2), 1 + max(leftHeight, rightHeight)

    return dfs(root)[0]


for root in inputs:
    print(main(root), end=' ')
