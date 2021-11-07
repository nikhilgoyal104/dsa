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


# T=n,S=1
def main(root):
    if not root:
        return None
    originalRoot = root
    while root.left:
        temp = root
        while temp:
            temp.left.next = temp.right
            if temp.next:
                temp.right.next = temp.next.left
            temp = temp.next
        root = root.left
    return originalRoot


print(main(build()))
