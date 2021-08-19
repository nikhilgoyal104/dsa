from binarytree import build as b


# T=n,S=d
def x(root):
    def dfs(root):
        return 1 + dfs(root.left) + dfs(root.right) if root else 0

    return dfs(root)


# T=d²,S=1
def y(root):
    def depth(root, right):
        d = 0
        while root:
            d += 1
            root = root.right if right else root.left
        return d

    def dfs(root):
        if not root:
            return 0
        left, right = depth(root, False), depth(root, True)
        if left == right:
            return 2 ** left - 1
        return 1 + dfs(root.left) + dfs(root.right)

    return dfs(root)


def depth(root):
    d = 0
    while root.left:
        d += 1
        root = root.left
    return d


def exists(index, d, root):
    low, high = 0, 2 ** d - 1
    for _ in range(d):
        mid = low + (high - low) // 2
        if index <= mid:
            high, root = mid, root.left
        else:
            low, root = mid + 1, root.right
    return root


# T=d²,S=1
def z(root):
    if not root:
        return 0
    d = depth(root)
    if not d:
        return 1
    low, high = 1, 2 ** d - 1
    while low <= high:
        mid = low + (high - low) // 2
        if exists(mid, d, root):
            low = mid + 1
        else:
            high = mid - 1
    return (2 ** d - 1) + low


for root in [
    b([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),
    b([1, 2, 3, 4, 5, 6]),
    b([]),
    b([1])
]:
    print(x(root), end=' ')
    print(y(root), end=' ')
    print(z(root))
