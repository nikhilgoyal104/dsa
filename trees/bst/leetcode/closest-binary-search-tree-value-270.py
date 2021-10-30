from binarytree import build
from math import inf

inputs = [
    (build([50, 25, 75, 12, 37, 62, 87, None, None, 30, None, None, 70, None, None]), 62.42),
    (build([50, 25, 75, 12, 37, 62, 87, None, None, 30, None, None, 70, None, None]), 75.48),
    (build([50, 25, 75, 12, 37, 62, 87, None, None, 30, None, None, 70, None, None]), 10),
    (build([50, 25, 75, 12, 37, 62, 87, None, None, 30, None, None, 70, None, None]), 90),
    (build([4, 2, 5, 1, 3]), 3.714286),
    (build([1]), 4.428571),
    (build([1]), -2.424),
    (build([1]), 1),
]


# T=n,S=n
def main(root, target):
    def dfs(root):
        return dfs(root.left) + [root.val] + dfs(root.right) if root else []

    return min(dfs(root), key=lambda x: abs(x - target))


for root, target in inputs:
    print(main(root, target), end=' ')

print()


# T=h,S=1
def main(root, target):
    res = root.val
    while root:
        res = min(res, root.val, key=lambda x: abs(x - target))
        root = root.right if target > root.val else root.left
    return res


for root, target in inputs:
    print(main(root, target), end=' ')
