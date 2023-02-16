from trees.generic.util import build

root = build([1, 2, 5, -1, 6, -1, -1, 3, 7, -1, 8, 11, -1, 12, -1, -1, 9, -1, -1, 4, 10, -1, -1, -1])


def main(root, data):
    def dfs(root, path):
        if root.val == data:
            return path
        for child in root.children:
            res = dfs(child, path + [child.data])
            if res:
                return res
        return []

    return dfs(root, [1])


for data in [11, 100]:
    print(main(root, data))

print()


def main(root, data):
    path = []

    def dfs(root):
        path.append(root.val)
        if root.val == data:
            return True
        for child in root.children:
            if dfs(child):
                return True
        path.pop()
        return False

    return dfs(root)


for data in [11, 100]:
    print(main(root, data))

print()


def main(root, data):
    path = []

    def dfs(root):
        path.append(root.val)
        if root.val == data:
            return True
        for child in root.children:
            if dfs(child):
                return path
        path.pop()
        return []

    return dfs(root)


for data in [11, 100]:
    print(main(root, data))

print()
