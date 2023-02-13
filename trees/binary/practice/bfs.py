from binarytree import build2
from collections import deque

inputs = [
    build2([50, 25, 75, 12, 37, 62, 87, None, None, 30, None, None, 70])
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
    print(root)
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
    print(root)
    main(root)
