from binarytree import build


# T=n
def main(root):
    def dfs(root):
        if not root:
            return 0
        return 1 + dfs(root.left) + dfs(root.right)

    return dfs(root)


for root in [
    build([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),
    build([1, 2, 3, 4, 5, 6]),
    build([]),
    build([1])
]:
    print(main(root), end=' ')

print()


def getLeftmostBranchHeight(root):
    res = 0
    while root:
        root = root.left
        res += 1
    return res


def getRightmostBranchHeight(root):
    res = 0
    while root:
        root = root.right
        res += 1
    return res


# T=(logn)²,S=1
def main(root):
    def dfs(root):
        if not root:
            return 0
        leftmostBranchHeight = getLeftmostBranchHeight(root)
        rightmostBranchHeight = getRightmostBranchHeight(root)
        if leftmostBranchHeight == rightmostBranchHeight:
            return 2 ** leftmostBranchHeight - 1
        return 1 + dfs(root.left) + dfs(root.right)

    return dfs(root)


for root in [
    build([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),
    build([1, 2, 3, 4, 5, 6]),
    build([]),
    build([1])
]:
    print(main(root), end=' ')
