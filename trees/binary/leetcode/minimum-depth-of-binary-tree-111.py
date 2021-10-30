from binarytree import build2
from collections import deque

inputs = [
    build2([1, 2, 3, 4, 5, 6, 7, None, None, 8, None, None, 9, None, None]),
    build2([3, 9, 20, None, None, 15, 7]),
    build2([2, None, 3, None, 4, None, 5, None, 6]),
    build2([])
]


# T=n
def bfs(root):
    if not root:
        return 0
    queue = deque([(root, 1)])
    while queue:
        node, dist = queue.popleft()
        if node.left is node.right:
            return dist
        if node.left:
            queue.append((node.left, dist + 1))
        if node.right:
            queue.append((node.right, dist + 1))


for root in inputs:
    print(bfs(root), end=' ')
