class Node:
    def __init__(self, val):
        self.val = val
        self.children = []


class Tree:
    def __init__(self):
        self.root = None


def build(lst):
    tree = Tree()
    node = Node(lst[0])
    tree.root = node
    stack = [node]
    for i in range(1, len(lst)):
        if lst[i] == -1:
            stack.pop()
            continue
        node = Node(lst[i])
        stack[-1].children.append(node)
        stack.append(node)
    return tree.root
