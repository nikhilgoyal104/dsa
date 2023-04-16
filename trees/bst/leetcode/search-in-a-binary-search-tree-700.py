from binarytree import build2

inputs = [
    (build2([4, 2, 7, 1, 3]), 2),
    (build2([4, 2, 7, 1, 3]), 5)
]


# T=h
def main(root, target):
    def dfs(root):
        if not root or target == root.val:
            return root
        if target > root.val:
            return dfs(root.right)
        return dfs(root.left)

    return dfs(root)


for root, target in inputs:
    print(main(root, target), end=' ')

print()


# T=h
def main(root, target):
    while root:
        if target == root.val:
            return root
        if target > root.val:
            root = root.right
        else:
            root = root.left
    return root


for root, target in inputs:
    print(main(root, target), end=' ')
