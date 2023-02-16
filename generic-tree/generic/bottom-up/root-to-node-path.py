from trees.generic.util import build

root = build([1, 2, 5, -1, 6, -1, -1, 3, 7, -1, 8, 11, -1, 12, -1, -1, 9, -1, -1, 4, 10, -1, -1, -1])


def main(root, val):
    def dfs(root):
        if root.val == val:
            return [root.val]
        res = []
        for child in root.children:
            path = dfs(child)
            if path:
                res = [root.val] + path
        return res

    return dfs(root)


for val in [11, 100]:
    print(main(root, val))
