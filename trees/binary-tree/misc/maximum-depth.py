from binarytree import build as b


def dfs(root):
    if not root:
        return -1
    return 1 + max(dfs(root.left), dfs(root.right))


for root in [
    b([1, 2, 3, 4, 5, 6, 7, None, None, 8, None, None, 9, None, None])
]:
    print(dfs(root))
