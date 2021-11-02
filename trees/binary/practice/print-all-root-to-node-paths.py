from binarytree import build2

inputs = [build2([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1])]
print(inputs[0])


def main(root):
    path = []

    def dfs(root):
        if not root:
            return
        path.append(root.val)
        print(path)
        dfs(root.left)
        dfs(root.right)
        path.pop()

    dfs(root)


for root in inputs:
    main(root)

print()


def main(root):
    def dfs(root, path):
        print(path)
        for child in [root.left, root.right]:
            if child:
                dfs(child, path + [child.val])

    dfs(root, [10])


for root in inputs:
    main(root)

print()


def main(root):
    def dfs(root, path):
        print(path)
        for child in [root.left, root.right]:
            if child:
                path.append(child.val)
                dfs(child, path)
                path.pop()

    dfs(root, [10])


for root in inputs:
    main(root)
