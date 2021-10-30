class Node:
    def __init__(self, val):
        self.val = val
        self.children = []


class Tree:
    def __init__(self):
        self.root = None


def build(values):
    n, tree = len(values), Tree()
    node = Node(values[0])
    tree.root, stack = node, [node]
    for i in range(1, n):
        if values[i] == -1:
            stack.pop()
            continue
        node = Node(values[i])
        stack[-1].children.append(node)
        stack.append(node)
    return tree.root
