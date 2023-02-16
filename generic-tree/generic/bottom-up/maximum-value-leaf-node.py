from trees.generic.util import build
from math import inf

root = build([1, 2, 5, -1, 6, -1, -1, 3, 7, -1, 8, 11, -1, 12, -1, -1, 9, -1, -1, 4, 10, -1, -1, -1])


def dfs(root):
    if not root.children:
        return root.val
    res = -inf
    for child in root.children:
        res = max(res, dfs(child))
    return res


print(dfs(root))
