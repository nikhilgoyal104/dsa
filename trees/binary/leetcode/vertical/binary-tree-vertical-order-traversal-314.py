from binarytree import build2
from collections import deque, defaultdict
from math import inf

inputs = [
    build2([3, 9, 20, None, None, 15, 7]),
    build2([3, 9, 8, 4, 0, 1, 7]),
    build2([3, 9, 8, 4, 0, 1, 7, None, None, None, 2, 5]),
    build2([]),
]


# T=nlogn,S=n
def main(root):
    if not root:
        return []
    queue = deque([(root, 0)])
    colIndexToValues = defaultdict(list)
    while queue:
        node, colIndex = queue.popleft()
        colIndexToValues[colIndex].append(node.val)
        for child, offset in (node.left, -1), (node.right, 1):
            if child:
                queue.append((child, colIndex + offset))
    return [colIndexToValues[colIndex] for colIndex in sorted(colIndexToValues)]


for root in inputs:
    print(main(root))

print()


# T=n,S=n
def main(root):
    if not root:
        return []
    queue = deque([(root, 0)])
    colIndexToValues = defaultdict(list)
    minColIndex, maxColIndex = inf, -inf
    while queue:
        node, colIndex = queue.popleft()
        minColIndex, maxColIndex = min(minColIndex, colIndex), max(maxColIndex, colIndex)
        colIndexToValues[colIndex].append(node.val)
        for child, offset in (node.left, -1), (node.right, 1):
            if child:
                queue.append((child, colIndex + offset))
    return [colIndexToValues[colIndex] for colIndex in range(minColIndex, maxColIndex + 1)]


for root in inputs:
    print(main(root))
