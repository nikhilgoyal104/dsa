from binarytree import build2
from math import inf


# T=n,S=h
def main(root):
    res = -inf

    def dfs(root):
        nonlocal res
        if not root:
            return 0
        left = dfs(root.left)
        right = dfs(root.right)
        res = max(res, root.val, left + root.val, right + root.val, left + right + root.val)
        return max(root.val, left + root.val, right + root.val)

    dfs(root)
    return res


for root in [
    build2([1, 2, 3]),
    build2([-10, 9, 20, None, None, 15, 7]),
    build2([2, -1]),
    build2([1]),
    build2([0]),
    build2([-3])
]:
    print(main(root))
