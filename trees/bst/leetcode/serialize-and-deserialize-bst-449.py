from binarytree import build2, Node as TreeNode


class Codec:

    def serialize(self, root):
        def dfs(root):
            if not root:
                return []
            return [root.val] + dfs(root.left) + dfs(root.right)

        return ','.join(map(str, dfs(root)))

    def deserialize(self, data):
        def dfs():
            pass

        return dfs()


codec = Codec()
for root in [
    build2([50, 25, 75, 12, 37, 62, 87, None, None, 30, None, None, 70]),
    build2([4, 2, 6, 1, 3, 5, 7]),
    build2([2, 1, 3]),
    build2([3, 1, 4, None, 2, None, 5]),
    build2([2, 1]),
    build2([1])
]:
    print(root)
    data = codec.serialize(root)
    print(data)
    print(codec.deserialize(data))
