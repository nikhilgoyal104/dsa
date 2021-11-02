from binarytree import build2, Node as TreeNode


class Codec:

    def serialize(self, root):
        def dfs(root):
            if not root:
                return []
            return dfs(root.left) + [root.val] + dfs(root.right)

        return ','.join(map(str, dfs(root)))

    def deserialize(self, data):
        inorder = data.split(',')

        def dfs(low, high):
            if low > high:
                return None
            mid = low + (high - low) // 2
            root = TreeNode(int(inorder[mid]))
            root.left = dfs(low, mid - 1)
            root.right = dfs(mid + 1, high)
            return root

        return dfs(0, len(inorder) - 1)


codec = Codec()
for root in [
    build2([50, 25, 75, 12, 37, 62, 87, None, None, 30, None, None, 70]),
    build2([4, 2, 6, 1, 3, 5, 7]),
    build2([2, 1, 3]),
    build2([])
]:
    print(root)
    data = codec.serialize(root)
    print(data)
    print(codec.deserialize(data))
