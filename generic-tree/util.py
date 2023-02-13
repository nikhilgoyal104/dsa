class Node:
    def __init__(self, data):
        self.val = data
        self.children = []


class Tree:
    def __init__(self):
        self.root = None


def construct(lst):
    n = len(lst)
    tree = Tree()
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
