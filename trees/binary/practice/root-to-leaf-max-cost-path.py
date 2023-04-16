from binarytree import build2


# T=n
def dfs(root):
    if not root:
        return 0
    return root.val + max(dfs(root.left), dfs(root.right))


for root in [
    build2([1, 2, 3, 4, 5, 6, 7, None, None, 8, None, None, 9]),
    build2([-1, -2, -3, -4, -5, -6, -7, None, None, -8, None, None, -9]),
]:
    print(dfs(root))
