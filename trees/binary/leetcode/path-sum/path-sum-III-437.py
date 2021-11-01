from binarytree import build2
from collections import Counter

inputs = [
    (build2([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1]), 8),
    (build2([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]), 22)
]


# T=n²
def main(root, target):
    res = 0

    def count(root, sum):
        nonlocal res
        if not root:
            return
        sum += root.val
        if sum == target:
            res += 1
        count(root.left, sum)
        count(root.right, sum)

    def dfs(root):
        if not root:
            return
        count(root, 0)
        dfs(root.left)
        dfs(root.right)

    dfs(root)
    return res


for root, target in inputs:
    print(main(root, target), end=' ')

print()


# T=n,S=n
def main(root, target):
    res, sumFreq = 0, Counter({0: 1})

    def dfs(root, sum):
        nonlocal res
        if not root:
            return
        sum += root.val
        res += sumFreq[sum - target]
        sumFreq[sum] += 1
        dfs(root.left, sum)
        dfs(root.right, sum)
        sumFreq[sum] -= 1

    dfs(root, 0)
    return res


for root, target in inputs:
    print(main(root, target), end=' ')
