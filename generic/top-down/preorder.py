from generic.util import build

root = build([1, 2, 5, -1, 6, -1, -1, 3, 7, -1, 8, 11, -1, 12, -1, -1, 9, -1, -1, 4, 10, -1, -1, -1])


def dfs(root):
    print(root.val, end=' ')
    for child in root.children:
        dfs(child)


print(dfs(root))
