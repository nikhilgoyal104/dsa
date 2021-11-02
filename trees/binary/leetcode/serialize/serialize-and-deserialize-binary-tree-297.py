from binarytree import Node as TreeNode, build2


# T=n,S=n
class Codec:

    def serialize(self, root):
        def dfs(root):
            if not root:
                return [None]
            return [root.val] + dfs(root.left) + dfs(root.right)

        return ','.join(map(str, dfs(root)))

    def deserialize(self, data):
        i, data = 0, data.split(',')

        def dfs():
            nonlocal i
            if data[i] == 'None':
                i += 1
                return None
            root = TreeNode(int(data[i]))
            i += 1
            root.left = dfs()
            root.right = dfs()
            return root

        return dfs()


codec = Codec()
for root in [
    build2([8, 3, 10, 1, 6, None, 14, None, None, 4, 7, 13]),
    build2([]),
    build2([1]),
    build2([1, 2]),
]:
    print(root)
    data = codec.serialize(root)
    print(codec.deserialize(data))
