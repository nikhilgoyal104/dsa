from binarytree import build2


# T=n
def main(root):
    def dfs(root, low, high):
        if not root:
            return True
        left = dfs(root.left, low, root.val)
        right = dfs(root.right, root.val, high)
        return low < root.val < high and left and right

    return dfs(root, float('-inf'), float('inf'))


for root in [
    build2([2, 1, 3]),
    build2([5, 1, 4, None, None, 3, 6]),
    build2([50, 25, 75, 12, 37, 62, 87, None, None, 30, None, None, 70, None, None]),
    build2([1, 2]),
    build2([2, 1])
]:
    print(main(root))
