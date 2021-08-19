from binarytree import build as b


# T=h
def x(root, target):
    def dfs(root):
        if not root or target == root.val:
            return root
        return dfs(root.right) if target > root.val else dfs(root.left)

    return dfs(root)


# T=h
def y(root, target):
    while root:
        if target == root.val:
            return root
        root = root.right if target > root.val else root.left
    return root


for root, target in [
    (b([4, 2, 7, 1, 3]), 2),
    (b([4, 2, 7, 1, 3]), 5)
]:
    print(x(root, target), end=' ')
    print(y(root, target))
