from binarytree import build2


def main(root):
    def dfs(root, sum):
        if not root:
            return False
        sum += root.val
        if root.left is root.right:
            return sum == target
        return dfs(root.left, sum) or dfs(root.right, sum)

    return dfs(root, 0)


for root, target in [
    (build2([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]), 22),
    (build2([1, 2, 3]), 5),
    (build2([1, 2]), 0)
]:
    print(main(root))
