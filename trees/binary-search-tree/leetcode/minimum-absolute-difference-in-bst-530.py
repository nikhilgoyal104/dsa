from binarytree import build as b
from math import inf


# T=n,S=n
def x(root):
    def dfs(root):
        return dfs(root.left) + [root.val] + dfs(root.right) if root else []

    nums = dfs(root)
    return min(nums[i + 1] - nums[i] for i in range(len(nums) - 1))


# T=n,S=1
def y(root):
    p = [-inf, inf]

    def dfs(root):
        if not root:
            return
        dfs(root.left)
        p[1], p[0] = min(p[1], root.val - p[0]), root.val
        dfs(root.right)

    dfs(root)
    return p[1]


# T=n,S=1
def z(root):
    def dfs(root, low, high):
        if not root:
            return inf
        left = dfs(root.left, low, root.val)
        right = dfs(root.right, root.val, high)
        return min(root.val - low, high - root.val, left, right)

    return dfs(root, -inf, inf)


for root in [
    b([4, 2, 6, 1, 3]),
    b([1, 0, 48, None, None, 12, 49])
]:
    print(x(root), end=' ')
    print(y(root), end=' ')
    print(z(root))
