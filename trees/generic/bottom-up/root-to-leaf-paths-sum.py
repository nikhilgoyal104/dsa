from trees.generic.util import build

root = build([1, 2, 5, -1, 6, -1, -1, 3, 7, -1, 8, 11, -1, 12, -1, -1, 9, -1, -1, 4, 10, -1, -1, -1])


def dfs(root):
    if not root.children:
        return [root.val]
    res = []
    for child in root.children:
        for sum in dfs(child):
            res.append(root.val + sum)
    return res


print(dfs(root))
