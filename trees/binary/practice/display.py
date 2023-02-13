from binarytree import build2


def main(root):
    def dfs(root):
        if not root:
            return
        print(root.val, end=' ')
        for child in [root.left, root.right]:
            dfs(child)

    dfs(root)


for root in [
    build2([50, 25, 75, 12, 37, 62, 57, None, None, 30, None, None, 70])
]:
    print(root)
    main(root)
