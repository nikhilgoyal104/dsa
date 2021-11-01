from binarytree import build2

inputs = [
    build2([1, 2, 3, 4, 5]),
    build2([1, 2]),
]


# T=n,S=h
def main(root):
    res = 0

    def dfs(root):
        nonlocal res
        if not root:
            return -1
        left = dfs(root.left)
        right = dfs(root.right)
        res = max(res, left + right + 2)
        return 1 + max(left, right)

    dfs(root)
    return res


for root in inputs:
    print(main(root))
