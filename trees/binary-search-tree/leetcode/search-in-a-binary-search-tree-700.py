from binarytree import build as b


# T=h
def x(root, tar):
    def dfs(root):
        if not root or tar == root.val:
            return root
        return dfs(root.right) if tar > root.val else dfs(root.left)

    return dfs(root)


# T=h
def y(root, tar):
    while root:
        if tar == root.val:
            return root
        root = root.right if tar > root.val else root.left
    return root


for root, tar in [
    (b([4, 2, 7, 1, 3]), 2),
    (b([4, 2, 7, 1, 3]), 5)
]:
    print(x(root, tar), end=' ')
    print(y(root, tar))
