from binarytree import build


def x(root, tar):
    def dfs(root):
        if not root:
            return False
        if tar == root.val:
            return True
        return dfs(root.right) if tar > root.val else dfs(root.left)

    return dfs(root)


def y(root, tar):
    while root:
        if tar == root.val:
            return True
        root = root.right if tar > root.val else root.left
    return False


for root, tar in [
    (build([4, 2, 7, 1, 3]), 2),
    (build([4, 2, 7, 1, 3]), 5)
]:
    print(x(root, tar), end=' ')
    print(y(root, tar))
