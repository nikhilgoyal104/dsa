from binarytree import build2

inputs = [build2([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1])]


def main(root):
    def dfs(root, sum):
        if not root:
            return
        sum += root.val
        print(sum, end=' ')
        dfs(root.left, sum)
        dfs(root.right, sum)

    dfs(root, 0)


for root in inputs:
    print(root)
    main(root)
