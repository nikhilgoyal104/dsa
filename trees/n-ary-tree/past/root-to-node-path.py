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


def x(root, data, path):
    if root.data == data:
        return path
    for ch in root.children:
        p = x(ch, data, path + [ch.data])
        if p:
            return p
    return []


def y(root, data, path):
    path.append(root.data)
    if root.data == data:
        return True
    for ch in root.children:
        if y(ch, data, path):
            return True
    path.pop()
    return False


def z(root, data, path):
    path.append(root.data)
    if root.data == data:
        return True
    for ch in root.children:
        if z(ch, data, path):
            return path
    path.pop()
    return []


root = construct([1, 2, 5, -1, 6, -1, -1, 3, 7, -1, 8, 11, -1, 12, -1, -1, 9, -1, -1, 4, 10, -1, -1, -1])
for data in [11, 100]:
    print(x(root, data, [1]))
    path = []
    y(root, data, path)
    print(path)
    print(z(root, data, []))
