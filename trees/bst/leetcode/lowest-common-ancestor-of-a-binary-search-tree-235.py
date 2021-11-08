from binarytree import build2

r1 = build2([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
r2 = build2([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
r3 = build2([2, 1])

inputs = [
    (r1, r1.left, r1.right),
    (r2, r2.left, r2.left.right.right),
    (r3, r3, r3.left)
]


# T=n,S=n
def main(root, p, q):
    def dfs(root):
        if p.val < root.val and q.val < root.val:
            return dfs(root.left)
        if p.val > root.val and q.val > root.val:
            return dfs(root.right)
        return root

    return dfs(root)


for root, p, q in inputs:
    print(main(root, p, q).val)
