from binarytree import build2

inputs = [
    (build2([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]), 22),
    (build2([1, 2, 3]), 5),
    (build2([1, 2]), 0)
]


def main(root, target):
    def dfs(root, sum):
        if not root:
            return []
        sum += root.val
        if root.left is root.right:
            return [[root.val]] if sum == target else []
        res = []
        for child in [root.left, root.right]:
            for path in dfs(child, sum):
                res.append([root.val] + path)
        return res

    return dfs(root, 0)


for root, target in inputs:
    print(main(root, target))
