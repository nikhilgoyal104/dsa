from binarytree import build2

inputs = [
    build2([1, 2, 3, None, 5]),
    build2([1]),
]


def main(root):
    def dfs(root):
        if not root:
            return []
        if root.left is root.right:
            return [[root.val]]
        res = []
        for child in [root.left, root.right]:
            for path in dfs(child):
                res.append([root.val] + path)
        return res

    return dfs(root)


for root in inputs:
    print(main(root))

print()


def main(root):
    def dfs(root):
        if not root:
            return ''
        if root.left is root.right:
            return [str(root.val)]
        res = []
        for child in [root.left, root.right]:
            for path in dfs(child):
                res.append(str(root.val) + '->' + path)
        return res

    return dfs(root)


for root in inputs:
    print(main(root))
