from binarytree import build2

r1 = build2([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
r2 = build2([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
r3 = build2([1, 2])
inputs = [
    (r1, r1.left, r1.right),
    (r2, r2.left, r2.left.right.right),
    (r3, r3, r3.left)
]


# T=n,S=n
def main(root, p, q):
    def dfs(root):
        if not root or root in [p, q]:
            return root
        left = dfs(root.left)
        right = dfs(root.right)
        if left and right:
            return root
        return left or right

    return dfs(root)


for root, p, q in inputs:
    print(main(root, p, q).val)
