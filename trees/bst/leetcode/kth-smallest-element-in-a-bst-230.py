from binarytree import build2

inputs = [
    (build2([3, 1, 4, None, 2]), 1),
    (build2([5, 3, 6, 2, 4, None, None, 1]), 1),
    (build2([5, 3, 6, 2, 4, None, None, 1]), 3),
]


# T=n,S=n
def main(root, k):
    def dfs(root):
        return dfs(root.left) + [root.val] + dfs(root.right) if root else []

    return dfs(root)[k - 1]


for root, k in inputs:
    print(main(root, k), end=' ')

print()


# T=h+k,S=h
def main(root, k):
    map = {
        'k': k,
        'res': None
    }

    def dfs(root):
        if not root or map['k'] < 0:
            return
        dfs(root.left)
        map['k'] -= 1
        if not map['k']:
            map['res'] = root.val
            return
        dfs(root.right)

    dfs(root)
    return map['res']


for root, k in inputs:
    print(main(root, k), end=' ')
