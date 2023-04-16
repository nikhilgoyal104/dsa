from binarytree import build2

inputs = [
    build2([4, 2, 6, 1, 3]),
    build2([1, 0, 48, None, None, 12, 49])
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
    map = {
        'prev': float('-inf'),
        'res': float('inf')
    }

    def dfs(root):
        if not root:
            return
        dfs(root.left)
        map['res'] = min(map['res'], root.val - map['prev'])
        map['prev'] = root.val
        dfs(root.right)

    dfs(root)
    return map['res']


for root in inputs:
    print(main(root), end=' ')

print()


# T=n,S=1
def main(root):
    def dfs(root, low, high):
        if not root:
            return float('inf')
        left = dfs(root.left, low, root.val)
        right = dfs(root.right, root.val, high)
        return min(root.val - low, high - root.val, left, right)

    return dfs(root, float('-inf'), float('inf'))


for root in inputs:
    print(main(root), end=' ')
