from binarytree import Node as TreeNode
from collections import deque


# T=n,S=n
def main(preorder, inorder):
    preorder = deque(preorder)
    valToIndex = {val: i for i, val in enumerate(inorder)}

    def dfs(low, high):
        if low > high:
            return None
        root = TreeNode(preorder[0])
        i = valToIndex[preorder.popleft()]
        root.left = dfs(low, i - 1)
        root.right = dfs(i + 1, high)
        return root

    return dfs(0, len(inorder) - 1)


for preorder, inorder in [
    ([3, 9, 20, 15, 7], [9, 3, 15, 20, 7]),
    ([0, 1, 3, 7, 8, 4, 9, 10, 2, 5, 11, 6], [7, 3, 8, 1, 9, 4, 10, 0, 11, 5, 2, 6]),
    ([-1], [-1]),
]:
    print(main(preorder, inorder))
