from binarytree import build

inputs = [
    (build([4, 2, 7, 1, 3]), 2),
    (build([4, 2, 7, 1, 3]), 5)
]


def main(root, target):
    def dfs(root):
        if not root:
            return False
        if target == root.val:
            return True
        return dfs(root.right) if target > root.val else dfs(root.left)

    return dfs(root)


for root, target in inputs:
    print(main(root, target))

print()


def main(root, target):
    while root:
        if target == root.val:
            return True
        root = root.right if target > root.val else root.left
    return False


for root, target in inputs:
    print(main(root, target))
