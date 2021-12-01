from binarytree import build2
from collections import deque, defaultdict
from math import inf
from heapq import heappop, heappush, heapify

inputs = [
    build2([3, 9, 20, None, None, 15, 7]),
    build2([1, 2, 3, 4, 5, 6, 7]),
    build2([1, 2, 3, 4, 6, 5, 7]),
    build2([0, 5, 1, 9, None, 2, None, None, None, None, 3, 4, 8, 6, None, None, None, 7]),
    build2([3, 1, 4, 0, 2, 2]),
    build2([0, 2, 1, 3, None, None, None, 4, 5, None, 7, 6, None, 10, 8, 11, 9]),
]


# T=nlogn,S=n
def main(root):
    queue = deque([(root, 0, 0)])
    colToValues = defaultdict(list)
    minCol, maxCol = inf, -inf
    while queue:
        node, row, col = queue.popleft()
        minCol, maxCol = min(minCol, col), max(maxCol, col)
        colToValues[col].append((row, node.val))
        for child, offset in (node.left, -1), (node.right, 1):
            if child:
                queue.append((child, row + 1, col + offset))
    res = []
    for col in range(minCol, maxCol + 1):
        res.append([val for _, val in sorted(colToValues[col])])
    return res


for root in inputs:
    print(main(root))
