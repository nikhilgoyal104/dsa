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


def main(root):
    def dfs(root):
        if not root.left and not root.right:
            return root
        left = dfs(root.left)
        right = dfs(root.right)
        left.next = right
        return root

    return dfs(root)


print(main(build()))
