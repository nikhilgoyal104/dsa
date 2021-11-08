from collections import deque


class Node:
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


def build():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(7)
    return root


# T=n,S=n
def main(root):
    if not root:
        return None
    queue = deque([root])
    while queue:
        size = len(queue)
        for i in range(size):
            node = queue.popleft()
            if i < size - 1:
                node.next = queue[0]
            for child in [node.left, node.right]:
                if child:
                    queue.append(child)
    return root


print(main(build()))


# T=n,S=1
def main(root):
    if not root:
        return None
    node = root
    dummy = Node(-1)
    while node:
        tail = dummy
        while node:
            if node.left:
                tail.next = node.left
                tail = tail.next
            if node.right:
                tail.next = node.right
                tail = tail.next
            node = node.next
        node = dummy.next
        dummy.next = None
    return root


print(main(build()))
