from binarytree import build
from math import inf


# T=n
def x(root):
    def dfs(root, low, high):
        if not root:
            return True
        return low < root.val < high and dfs(root.left, low, root.val) and dfs(root.right, root.val, high)

    return dfs(root, -inf, inf)


# T=n
def y(root):
    prev = [-inf]

    def dfs(root):
        if not root:
            return True
        if not dfs(root.left):
            return False
        if root.val <= prev[0]:
            return False
        prev[0] = root.val
        return dfs(root.right)

    return dfs(root)


# T=n
def z(root):
    stack, prev = [], -inf
    while stack or root:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        if root.val <= prev:
            return False
        prev, root = root.val, root.right
    return True


for root in [
    build([2, 1, 3]),
    build([5, 1, 4, None, None, 3, 6]),
    build([50, 25, 75, 12, 37, 62, 87, None, None, 30, None, None, 70, None, None]),
    build([1, 2]),
    build([2, 1])
]:
    print(x(root), end=' ')
    print(y(root), end=' ')
    print(z(root))
