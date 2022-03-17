from binarytree import build2
from collections import deque
from math import inf


# T=n,S=n
def main(root):
    if not root:
        return []
    res, colToValues = [], {}
    queue = deque([(root, 0)])
    minCol, maxCol = inf, -inf
    while queue:
        node, col = queue.popleft()
        minCol, maxCol = min(minCol, col), max(maxCol, col)
        colToValues[col] = node.val
        for child, offset in (node.left, -1), (node.right, 1):
            if child:
                queue.append((child, col + offset))
    for col in range(minCol, maxCol + 1):
        res.append(colToValues[col])
    return res


for root in [
    build2([20, 8, 22, 5, 3, None, 25, None, None, 10, 14]),
    build2([20, 8, 22, 5, 3, 4, 25, None, None, 10, 14]),
    build2([1, 2, 3, 4, 5, 6, 7, None, 8, 9, None, None, 10, None, 11]),
]:
    print(main(root))
