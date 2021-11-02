from collections import defaultdict
from binarytree import build2
from pprint import pprint

root = build2([1, 2, 3, 4, 5, 6, 7, None, None, 8, None, None, 9])
print(root)


def main(root):
    graph = defaultdict(list)

    def dfs(root, parent):
        if not root:
            return
        if parent:
            graph[root.val].append(parent.val)
            graph[parent.val].append(root.val)
        dfs(root.left, root)
        dfs(root.right, root)

    dfs(root, None)
    return graph


pprint(main(root))


def main(root):
    graph = defaultdict(list)

    def dfs(root, parent):
        if not root:
            return
        if root.left is root.right:
            graph[root.val] = []
        if parent:
            graph[parent.val].append(root.val)
        dfs(root.left, root)
        dfs(root.right, root)

    dfs(root, None)
    return graph


pprint(main(root), width=30)
