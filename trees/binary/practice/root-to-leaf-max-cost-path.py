from binarytree import build


# T=n
def dfs(root):
    if not root:
        return 0
    return root.val + max(dfs(root.left), dfs(root.right))


for root in [
    build([1, 2, 3, 4, 5, 6, 7, None, None, 8, None, None, 9]),
    build([-1, -2, -3, -4, -5, -6, -7, None, None, -8, None, None, -9]),
]:
    print(dfs(root))
