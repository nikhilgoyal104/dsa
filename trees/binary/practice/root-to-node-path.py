from binarytree import build2


def main(root, target):
    def dfs(root):
        if not root:
            return []
        if root.val == target:
            return [root.val]
        for child in [root.left, root.right]:
            path = dfs(child)
            if path:
                return [root.val] + path
        return []

    return dfs(root)


for root, target in [
    (build2([1, 2, 3, 4, 5, 6, 7, None, None, 8, None, None, 9]), 10),
    (build2([1, 2, 3, 4, 5, 6, 7, None, None, 8, None, None, 9]), 9),
    (build2([1, 2, 3, 4, 5, 6, 7, None, None, 8, None, None, 9]), 7),
]:
    print(main(root, target))
