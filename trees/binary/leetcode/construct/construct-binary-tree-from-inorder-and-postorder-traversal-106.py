from binarytree import Node as TreeNode


# T=n,S=n
def main(inorder, postorder):
    valToIndex = {val: i for i, val in enumerate(inorder)}

    def dfs(low, high):
        if low > high:
            return None
        root = TreeNode(postorder[-1])
        i = valToIndex[postorder.pop()]
        root.right = dfs(i + 1, high)
        root.left = dfs(low, i - 1)
        return root

    return dfs(0, len(inorder) - 1)


for inorder, postorder in [
    ([9, 3, 15, 20, 7], [9, 15, 7, 20, 3]),
    ([-1], [-1]),
]:
    print(main(inorder, postorder))
