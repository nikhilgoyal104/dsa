from trees.generic.util import build

root = build([1, 2, 5, -1, 6, -1, -1, 3, 7, -1, 8, 11, -1, 12, -1, -1, 9, -1, -1, 4, 10, -1, -1, -1])


def main(root, k):
    def dfs(root, k):
        if not k:
            return [[root.val]]
        res = []
        for child in root.children:
            for path in dfs(child, k - 1):
                res.append([root.val] + path)
        return res

    return dfs(root, k)


for k in [2, 3]:
    print(main(root, k))
