from binarytree import build2, Node as TreeNode
from collections import deque
from math import inf


# T=n,S=n
class Codec:

    def serialize(self, root):
        def dfs(root):
            if not root:
                return []
            return [root.val] + dfs(root.left) + dfs(root.right)

        return ','.join(map(str, dfs(root)))

    def deserialize(self, data):
        queue = deque([int(val) for val in data.split(',') if val])

        def dfs(low, high):
            if not queue or int(queue[0]) < low or int(queue[0]) > high:
                return None
            val = int(queue.popleft())
            root = TreeNode(val)
            root.left = dfs(low, val)
            root.right = dfs(val, high)
            return root

        return dfs(-inf, inf)


codec = Codec()
for root in [
    build2([50, 25, 75, 12, 37, 62, 87, None, None, 30, None, None, 70]),
    build2([4, 2, 6, 1, 3, 5, 7]),
    build2([2, 1, 3]),
    build2([3, 1, 4, None, 2, None, 5]),
    build2([2, 1]),
    build2([1]),
    build2([]),
]:
    print(root)
    data = codec.serialize(root)
    print(codec.deserialize(data))
