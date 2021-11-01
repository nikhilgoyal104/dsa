from binarytree import build2
from math import inf


# T=n,S=h
def main(root):
    res = -inf

    def dfs(root):
        nonlocal res
        if not root:
            return 0
        maxPathSumLeft = dfs(root.left)
        maxPathSumRight = dfs(root.right)
        res = max(res, root.val, maxPathSumLeft + root.val, maxPathSumRight + root.val,
                  maxPathSumLeft + maxPathSumRight + root.val)
        return max(root.val, maxPathSumLeft + root.val, maxPathSumRight + root.val)

    dfs(root)
    return res


for root in [
    build2([1, 2, 3]),
    build2([-10, 9, 20, None, None, 15, 7]),
    build2([2, -1]),
    build2([1]),
    build2([0]),
    build2([-3]),
    build2([9, 6, -3, None, None, -6, 2, None, None, 2, None, -6, -6, -6])
]:
    print(main(root))
