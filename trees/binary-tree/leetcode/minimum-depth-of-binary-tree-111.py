from binarytree import build


# T=n
def dfs(root):
    if not root:
        return 0
    left = right = 0
    if root.left:
        left = 1 + dfs(root.left)
    if root.right:
        right = 1 + dfs(root.right)
    return min(left, right)


for root in [
    build([1, 2, 3, 4, 5, 6, 7, None, None, 8, None, None, 9, None, None])
]:
    print(root)
    print(dfs(root))
