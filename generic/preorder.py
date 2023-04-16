from util import build


def main(root):
    def dfs(root):
        res = [root.val]
        for child in root.children:
            res += dfs(child)
        return res

    return dfs(root)


root = build([1, 2, 5, -1, 6, -1, -1, 3, 7, -1, 8, 11, -1, 12, -1, -1, 9, -1, -1, 4, 10, -1, -1, -1])
print(main(root))
