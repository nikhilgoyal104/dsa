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


def y(root, path):
    if not root.children:
        return [path]
    res = []
    for ch in root.children:
        res += y(ch, path + [ch.data])
    return res


def z(root, path):
    if not root.children:
        return [path[:]]
    res = []
    for ch in root.children:
        path.append(ch.data)
        res += z(ch, path)
        path.pop()
    return res


root = construct([1, 2, 5, -1, 6, -1, -1, 3, 7, -1, 8, 11, -1, 12, -1, -1, 9, -1, -1, 4, 10, -1, -1, -1])
print(y(root, [1]))
print(z(root, [1]))
