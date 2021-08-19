def construct(lst):
    n, tree = len(lst), Tree()
    node = Node(lst[0])
    tree.root, stack = node, [node]
    for i in range(1, n):
        if lst[i] == -1:
            stack.pop()
            continue
        node = Node(lst[i])
        stack[-1].children.append(node)
        stack.append(node)
    return tree.root


class Node:
    def __init__(self, data):
        self.data = data
        self.children = []


class Tree:
    def __init__(self):
        self.root = None


def x(root, k):
    if not k - 1:
        return [[root.data]]
    res = []
    for ch in root.children:
        for path in x(ch, k - 1):
            res.append([root.data] + path)
    return res


root = construct([1, 2, 5, -1, 6, -1, -1, 3, 7, -1, 8, 11, -1, 12, -1, -1, 9, -1, -1, 4, 10, -1, -1, -1])
print(x(root, 2))
print(x(root, 3))
