from binarytree import build2, Node as TreeNode


# T=h,S=h
def main(root, val):
    def dfs(root):
        if not root:
            return TreeNode(val)
        if val > root.val:
            root.right = dfs(root.right)
        else:
            root.left = dfs(root.left)
        return root

    return dfs(root)


for root, val in [
    (build2([4, 2, 7, 1, 3]), 5),
    (build2([40, 20, 60, 10, 30, 50, 70]), 25),
    (build2([4, 2, 7, 1, 3]), 5)
]:
    print(main(root, val))

print()


# T=h,S=h
def main(root, val):
    if not root:
        return TreeNode(val)
    node = root
    parent = None
    while node:
        parent = node
        node = node.right if val > node.val else node.left
    if val > parent.val:
        parent.right = TreeNode(val)
    else:
        parent.left = TreeNode(val)
    return root


for root, val in [
    (build2([4, 2, 7, 1, 3]), 5),
    (build2([40, 20, 60, 10, 30, 50, 70]), 25),
    (build2([4, 2, 7, 1, 3]), 5)
]:
    print(main(root, val))
