from binarytree import build as b
from math import inf


# T=n,S=n
def u(root, tar):
    def dfs(root):
        return dfs(root.left) + [root.val] + dfs(root.right) if root else []

    return min(dfs(root), key=lambda x: abs(x - tar))


# T=h+k,S=h
def v(root, tar):
    prev = [-inf]

    def dfs(root):
        if not root:
            return None
        left = dfs(root.left)
        if left:
            return left
        if prev[0] <= tar < root.val:
            return min(prev[0], root.val, key=lambda x: abs(tar - x))
        prev[0] = root.val
        return dfs(root.right)

    res = dfs(root)
    return res if res else prev[0]


# T=h+k,S=h
def w(root, tar):
    stack, prev = [], -inf
    while stack or root:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        if prev <= tar < root.val:
            return min(prev, root.val, key=lambda x: abs(tar - x))
        prev, root = root.val, root.right
    return prev


# T=h
def x(root, tar):
    closest = [inf]

    def dfs(root):
        if not root:
            return
        closest[0] = min(closest[0], root.val, key=lambda x: abs(tar - x))
        if tar > root.val:
            dfs(root.right)
        else:
            dfs(root.left)

    dfs(root)
    return closest[0]


# T=h
def y(root, tar):
    closest = inf
    while root:
        closest = min(closest, root.val, key=lambda x: abs(tar - x))
        root = root.right if tar > root.val else root.left
    return closest


# T=h
def z(root, tar):
    def dfs(root, closest):
        if not root:
            return closest
        closest = min(closest, root.val, key=lambda x: abs(tar - x))
        if tar > root.val:
            closest = dfs(root.right, closest)
        return dfs(root.left, closest)

    return dfs(root, inf)


for root, tar in [
    (b([50, 25, 75, 12, 37, 62, 87, None, None, 30, None, None, 70, None, None]), 62.42),
    (b([50, 25, 75, 12, 37, 62, 87, None, None, 30, None, None, 70, None, None]), 75.48),
    (b([50, 25, 75, 12, 37, 62, 87, None, None, 30, None, None, 70, None, None]), 10),
    (b([50, 25, 75, 12, 37, 62, 87, None, None, 30, None, None, 70, None, None]), 90),
    (b([4, 2, 5, 1, 3]), 3.714286),
    (b([1]), 4.428571),
    (b([1]), -2.424),
    (b([1]), 1),
]:
    print(u(root, tar), end=' ')
    print(v(root, tar), end=' ')
    print(w(root, tar), end=' ')
    print(x(root, tar), end=' ')
    print(y(root, tar), end=' ')
    print(z(root, tar))
