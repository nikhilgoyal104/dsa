from binarytree import build
from math import inf


# T=n,S=n
def u(root, target):
    def dfs(root):
        return dfs(root.left) + [root.val] + dfs(root.right) if root else []

    return min(dfs(root), key=lambda x: abs(x - target))


# T=h+k,S=h
def v(root, target):
    prev = [-inf]

    def dfs(root):
        if not root:
            return None
        left = dfs(root.left)
        if left:
            return left
        if prev[0] <= target < root.val:
            return min(prev[0], root.val, key=lambda x: abs(target - x))
        prev[0] = root.val
        return dfs(root.right)

    res = dfs(root)
    return res if res else prev[0]


# T=h+k,S=h
def w(root, target):
    stack, prev = [], -inf
    while stack or root:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        if prev <= target < root.val:
            return min(prev, root.val, key=lambda x: abs(target - x))
        prev, root = root.val, root.right
    return prev


# T=h
def x(root, target):
    closest = [inf]

    def dfs(root):
        if not root:
            return
        closest[0] = min(closest[0], root.val, key=lambda x: abs(target - x))
        if target > root.val:
            dfs(root.right)
        else:
            dfs(root.left)

    dfs(root)
    return closest[0]


# T=h
def y(root, target):
    closest = inf
    while root:
        closest = min(closest, root.val, key=lambda x: abs(target - x))
        root = root.right if target > root.val else root.left
    return closest


# T=h
def z(root, target):
    def dfs(root, closest):
        if not root:
            return closest
        closest = min(closest, root.val, key=lambda x: abs(target - x))
        if target > root.val:
            closest = dfs(root.right, closest)
        return dfs(root.left, closest)

    return dfs(root, inf)


for root, target in [
    (build([50, 25, 75, 12, 37, 62, 87, None, None, 30, None, None, 70, None, None]), 62.42),
    (build([50, 25, 75, 12, 37, 62, 87, None, None, 30, None, None, 70, None, None]), 75.48),
    (build([50, 25, 75, 12, 37, 62, 87, None, None, 30, None, None, 70, None, None]), 10),
    (build([50, 25, 75, 12, 37, 62, 87, None, None, 30, None, None, 70, None, None]), 90),
    (build([4, 2, 5, 1, 3]), 3.714286),
    (build([1]), 4.428571),
    (build([1]), -2.424),
    (build([1]), 1),
]:
    print(u(root, target), end=' ')
    print(v(root, target), end=' ')
    print(w(root, target), end=' ')
    print(x(root, target), end=' ')
    print(y(root, target), end=' ')
    print(z(root, target))
