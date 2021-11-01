from binarytree import build2


# T=n,S=h
def main(root):
    def dfs(root, num):
        if not root:
            return 0
        num = num * 10 + root.val
        if root.left is root.right:
            return num
        left = dfs(root.left, num)
        right = dfs(root.right, num)
        return left + right

    return dfs(root, 0)


for root in [
    build2([1, 2, 3]),
    build2([4, 9, 0, 5, 1])
]:
    print(main(root))
