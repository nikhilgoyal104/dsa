from binarytree import tree, Node, build

print(tree())
print(tree(is_perfect=True))

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print(root)

print(root.properties)
print(root.leaves)
print(root.levels)

original = tree()
clone = original.clone()
print(original.equals(clone))

print(root.inorder)
print(root.preorder)
print(root.postorder)

print(root.values)

print(list(root))
print(root.levelorder)

root = build([7, 3, 2, 6, 9, None, 1, 5, 8])
print(root)
print(root.values)

root = build([7, 3, 2, 6, 9, 1, 5, 8])
print(root)
