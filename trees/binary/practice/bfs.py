from binarytree import build
from collections import deque

inputs = [
    build([50, 25, 75, 12, 37, 62, 87, None, None, 30, None, None, 70, None, None])
]


def main(root):
    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.val, end=' ')
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)


for root in inputs:
    main(root)

print()


def main(root):
    queue = deque([root])
    while queue:
        for _ in range(len(queue)):
            node = queue.popleft()
            print(node.val, end=' ')
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        print()


for root in inputs:
    main(root)
