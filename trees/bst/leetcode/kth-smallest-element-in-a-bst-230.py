from binarytree import build


# T=n,S=n
def v(root, k):
    def dfs(root):
        return dfs(root.left) + [root.val] + dfs(root.right) if root else []

    return dfs(root)[k - 1]


# T=h+k,S=h
def w(root, k):
    p = [k, None]

    def dfs(root):
        if not root or p[0] < 0:
            return
        dfs(root.left)
        p[0] -= 1
        if not p[0]:
            p[1] = root.val
            return
        dfs(root.right)

    dfs(root)
    return p[1]


# T=h+k,S=h
def x(root, k):
    c = [k]

    def dfs(root):
        if not root:
            return None
        left = dfs(root.left)
        if left:
            return left
        c[0] -= 1
        if not c[0]:
            return root
        return dfs(root.right)

    return dfs(root).val


# T=h+k,S=h
def y(root, k):
    def dfs(root, k):
        if not root:
            return None, k
        left, k = dfs(root.left, k)
        if left:
            return left, k
        k -= 1
        if not k:
            return root, k
        return dfs(root.right, k)

    return dfs(root, k)[0].val


# T=h+k,S=h
def z(root, k):
    stack = []
    while root or stack:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        k -= 1
        if not k:
            return root.val
        root = root.right


for root, k in [
    (build([3, 1, 4, None, 2]), 1),
    (build([5, 3, 6, 2, 4, None, None, 1]), 1),
    (build([5, 3, 6, 2, 4, None, None, 1]), 3),
]:
    print(v(root, k), end=' ')
    print(w(root, k), end=' ')
    print(x(root, k), end=' ')
    print(y(root, k), end=' ')
    print(z(root, k))
