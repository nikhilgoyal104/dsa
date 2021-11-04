from binarytree import build2, Node as TreeNode


# T=n,S=1
def main(root):
    if not root:
        return None
    dummy = tail = TreeNode(-1)

    def dfs(root):
        nonlocal tail
        if not root:
            return
        dfs(root.left)
        tail.right = root
        root.left = tail
        tail = tail.right
        dfs(root.right)

    dfs(root)
    tail.right = dummy.right
    dummy.right.left = tail
    return dummy.right


def display(head):
    if head is None:
        return
    temp = head
    while temp.right != head:
        print(temp.val, end=' ')
        temp = temp.right
    print(temp.val, end=' ')


for root in [
    build2([4, 2, 5, 1, 3]),
    build2([2, 1, 3]),
    build2([1]),
    build2([])
]:
    display(main(root))
    print()
