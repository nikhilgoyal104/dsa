from trees.generic.util import build

root = build([1, 2, 5, -1, 6, -1, -1, 3, 7, -1, 8, 11, -1, 12, -1, -1, 9, -1, -1, 4, 10, -1, -1, -1])


def main(root):
    def dfs(root, path):
        if not root.children:
            return [path]
        res = []
        for child in root.children:
            res += dfs(child, path + [child.data])
        return res

    return dfs(root, [1])


print(main(root))


def main(root):
    def dfs(root, path):
        if not root.children:
            return [path[:]]
        res = []
        for child in root.children:
            path.append(child.data)
            res += dfs(child, path)
            path.pop()
        return res

    return dfs(root, [1])


print(main(root))
