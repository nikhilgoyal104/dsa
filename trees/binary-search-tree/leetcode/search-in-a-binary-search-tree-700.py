from binarytree import build


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
    (build([4, 2, 7, 1, 3]), 2),
    (build([4, 2, 7, 1, 3]), 5)
]:
    print(x(root, target), end=' ')
    print(y(root, target))
