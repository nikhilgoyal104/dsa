from binarytree import build
from math import inf

inputs = [
    build([4, 2, 6, 1, 3]),
    build([1, 0, 48, None, None, 12, 49])
]


# T=n,S=n
def main(root):
    def dfs(root):
        return dfs(root.left) + [root.val] + dfs(root.right) if root else []

    nums = dfs(root)
    return min(nums[i + 1] - nums[i] for i in range(len(nums) - 1))


for root in inputs:
    print(main(root), end=' ')

print()


# T=n,S=1
def main(root):
    hm = {'prev': -inf, 'res': inf}

    def dfs(root):
        if not root:
            return
        dfs(root.left)
        hm['res'] = min(hm['res'], root.val - hm['prev'])
        hm['prev'] = root.val
        dfs(root.right)

    dfs(root)
    return hm['res']


for root in inputs:
    print(main(root), end=' ')

print()


# T=n,S=1
def main(root):
    def dfs(root, low, high):
        if not root:
            return inf
        left = dfs(root.left, low, root.val)
        right = dfs(root.right, root.val, high)
        return min(root.val - low, high - root.val, left, right)

    return dfs(root, -inf, inf)


for root in inputs:
    print(main(root), end=' ')
