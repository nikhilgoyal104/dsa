from binarytree import build2
from collections import deque


# T=n,S=n
def main(root):
    if not root:
        return []
    res, queue = [], deque([root])
    while queue:
        res.append(queue[-1].val)
        for _ in range(len(queue)):
            node = queue.popleft()
            for child in [node.left, node.right]:
                if child:
                    queue.append(child)
    return res


for root in [
    build2([1, 2, 3, None, 5, None, 4]),
    build2([]),
]:
    print(main(root))
