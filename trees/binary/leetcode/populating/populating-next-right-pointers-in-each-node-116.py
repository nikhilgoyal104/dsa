class TreeNode:
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


def build():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    return root


# T=n,S=h
def main(root):
    if not root:
        return None

    def dfs(root):
        if not root or not root.left:
            return
        root.left.next = root.right
        root.right.next = root.next.left if root.next else None
        dfs(root.left)
        dfs(root.right)

    dfs(root)


print(main(build()))


# T=n,S=1
def main(root):
    if not root:
        return None
    leftMost = root
    while leftMost.left:
        head = leftMost
        while head:
            head.left.next = head.right
            head.right.next = head.next.left if head.next else None
            head = head.next
        leftMost = leftMost.left
    return root


print(main(build()))
