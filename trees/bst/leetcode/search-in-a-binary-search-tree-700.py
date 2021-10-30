from binarytree import build

inputs = [
    (build([4, 2, 7, 1, 3]), 2),
    (build([4, 2, 7, 1, 3]), 5)
]


# T=h
def main(root, target):
    def dfs(root):
        if not root or target == root.val:
            return root
        return dfs(root.right) if target > root.val else dfs(root.left)

    return dfs(root)


for root, target in inputs:
    print(main(root, target), end=' ')

print()


# T=h
def main(root, target):
    while root:
        if target == root.val:
            return root
        root = root.right if target > root.val else root.left
    return root


for root, target in inputs:
    print(main(root, target), end=' ')
