from trees.generic.util import build
from collections import deque

root = build([1, 2, 5, -1, 6, -1, -1, 3, 7, -1, 8, 11, -1, 12, -1, -1, 9, -1, -1, 4, 10, -1, -1, -1])


def dfs(root):
    res = 0
    for child in root.children:
        res = max(res, 1 + dfs(child))
    return res


def bfs(root):
    queue, res = deque([root]), -1
    while queue:
        for _ in range(len(queue)):
            queue.extend(queue.popleft().children)
        res += 1
    return res


print(dfs(root))
print(bfs(root))
