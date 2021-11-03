from binarytree import build


# T=n
def main(root):
    def dfs(root):
        return 1 + dfs(root.left) + dfs(root.right) if root else 0

    return dfs(root)


for root in [
    build([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),
    build([1, 2, 3, 4, 5, 6]),
    build([]),
    build([1])
]:
    print(main(root), end=' ')

print()


def getLBH(root):
    count = 0
    while root:
        root = root.left
        count += 1
    return count


def getRBH(root):
    count = 0
    while root:
        root = root.right
        count += 1
    return count


# T=(logn)²,S=1
def main(root):
    def dfs(root):
        if not root:
            return 0
        lbh = getLBH(root)
        rbh = getRBH(root)
        if lbh == rbh:
            return 2 ** lbh - 1
        return 1 + dfs(root.left) + dfs(root.right)

    return dfs(root)


for root in [
    build([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),
    build([1, 2, 3, 4, 5, 6]),
    build([]),
    build([1])
]:
    print(main(root), end=' ')
