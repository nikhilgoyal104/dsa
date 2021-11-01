from trees.generic.util import build

root = build([1, 2, 5, -1, 6, -1, -1, 3, 7, -1, 8, 11, -1, 12, -1, -1, 9, -1, -1, 4, 10, -1, -1, -1])


def main(root):
    path = []

    def dfs(root):
        path.append(root.val)
        print(path, end=' ')
        for child in root.children:
            dfs(child)
        path.pop()

    dfs(root)


main(root)

print()


def main(root):
    def dfs(root, path):
        print(path, end=' ')
        for child in root.children:
            dfs(child, path + [child.val])

    dfs(root, [1])


main(root)

print()


def main(root):
    path = [1]

    def dfs(root):
        print(path, end=' ')
        for child in root.children:
            path.append(child.val)
            dfs(child)
            path.pop()

    dfs(root)


main(root)
