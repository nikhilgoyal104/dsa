from binarytree import build2

root = build2([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
print(root)


def ancestors(root, target):
    def dfs(root):
        if not root:
            return []
        if root == target:
            return [root.val]
        for child in [root.left, root.right]:
            path = dfs(child)
            if path:
                return [root.val] + path
        return []

    return dfs(root)


def distance(root, k):
    if not root:
        return []
    if not k:
        return [root.val]
    return distance(root.left, k - 1) + distance(root.right, k - 1)


def main(root, target, k):
    print(distance(target, k))
    print(ancestors(root, target))


for root, target, k in [
    (root, root.left, 2)
]:
    main(root, target, k)
