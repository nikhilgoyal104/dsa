from binarytree import build2
from math import inf

inputs = [
    build2([3, 1, 4, 3, None, 1, 5])
]


# T=n,S=h
def main(root):
    res = 0

    def dfs(root, largest):
        nonlocal res
        if not root:
            return
        largest = max(largest, root.val)
        if root.val == largest:
            res += 1
        dfs(root.left, largest)
        dfs(root.right, largest)

    dfs(root, -inf)
    return res


for root in inputs:
    print(main(root))


# T=n,S=h
def main(root):
    def dfs(root, largest):
        if not root:
            return 0
        largest = max(largest, root.val)
        return int(root.val == largest) + dfs(root.left, largest) + dfs(root.right, largest)

    return dfs(root, -inf)


for root in inputs:
    print(main(root))
