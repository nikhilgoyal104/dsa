from collections import deque
from binarytree import build as b, Node


def insetInLevelOrder(root, val):
    if not root:
        return Node(val)
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node.left:
            queue.append(node.left)
        else:
            node.left = Node(val)
            return root
        if node.right:
            queue.append(node.right)
        else:
            node.right = Node(val)
            return root


for root in [
    b([1, 2, 3, 4, 5, 6, 7, None, None, 8, None, None, 9, None, None])
]:
    print(insetInLevelOrder(root, 12))
