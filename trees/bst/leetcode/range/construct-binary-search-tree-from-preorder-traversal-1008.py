from binarytree import Node as TreeNode
from collections import deque
from math import inf


# T=n,S=n
def main(preorder):
    queue = deque(preorder)

    def dfs(low, high):
        if not queue or queue[0] < low or queue[0] > high:
            return None
        val = queue.popleft()
        root = TreeNode(val)
        root.left = dfs(low, val)
        root.right = dfs(val, high)
        return root

    return dfs(-inf, inf)


for preorder in [
    [8, 5, 1, 7, 10, 12],
    [1, 3]
]:
    print(main(preorder))
