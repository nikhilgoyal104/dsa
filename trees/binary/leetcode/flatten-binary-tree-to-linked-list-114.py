from binarytree import build2, Node as TreeNode


def display(head):
    temp = head
    while temp:
        print(temp.val, end=' ')
        temp = temp.right
    print()


def getLeftTail(leftHead):
    leftTail = leftHead
    while leftTail.right:
        leftTail = leftTail.right
    return leftTail


# T=n²,S=n
def main(root):
    def dfs(root):
        if not root:
            return None
        leftHead = dfs(root.left)
        rightHead = dfs(root.right)
        if leftHead:
            getLeftTail(leftHead).right = rightHead
            root.right = leftHead
        root.left = None
        return root

    return dfs(root)


for root in [
    build2([1, 2, 5, 3, 4, None, 6]),
    build2([]),
    build2([0]),
]:
    display(main(root))

print()


# T=n,S=n
def main(root):
    def dfs(root):
        if not root:
            return None
        if not root.left and not root.right:
            return root
        leftTail = dfs(root.left)
        rightTail = dfs(root.right)
        if leftTail:
            leftTail.right = root.right
            root.right = root.left
            root.left = None
        return rightTail if rightTail else leftTail

    return dfs(root)


for root in [
    build2([1, 2, 5, 3, 4, None, 6]),
    build2([]),
    build2([0]),
]:
    main(root)
