from binarytree import build2, Node as TreeNode

r1 = build2([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
r2 = build2([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
r3 = build2([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
inputs = [
    (r1, r1.left, r1.right),
    (r2, r2.left, r2.left.right.right),
    (r3, r3.left, TreeNode(10))
]


# T=n,S=n
def main(root, p, q):
    count = 0

    def dfs(root):
        nonlocal count
        if not root:
            return None
        left = dfs(root.left)
        right = dfs(root.right)
        if root in [p, q]:
            count += 1
            return root
        if left and right:
            return root
        return left or right

    lca = dfs(root)
    return lca if count == 2 else None


for root, p, q in inputs:
    lca = main(root, p, q)
    if lca:
        print(lca.val)
    else:
        print(lca)


def find(root, target):
    def dfs(root):
        if not root:
            return False
        if root is target:
            return True
        return dfs(root.left) or dfs(root.right)

    return dfs(root)


print()


# T=n,S=n
def main(root, p, q):
    def dfs(root):
        if root in [None, p, q]:
            return root
        left = dfs(root.left)
        right = dfs(root.right)
        if left and right:
            return root
        return left or right

    lca = dfs(root)
    if lca is p:
        return p if find(p, q) else None
    if lca is q:
        return q if find(q, p) else None
    return lca


for root, p, q in inputs:
    lca = main(root, p, q)
    if lca:
        print(lca.val)
    else:
        print(lca)
