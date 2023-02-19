from binarytree import build


# T=n,S=n
def main(root):
    cache = {None: 0}

    def dfs(root):
        if root in cache:
            return cache[root]
        inc, exc = root.val, 0
        for child in [root.left, root.right]:
            inc += dfs(child.left) + dfs(child.right) if child else 0
            exc += dfs(child)
        cache[root] = max(inc, exc)
        return cache[root]

    return dfs(root)


for root in [
    build([3, 2, 3, None, 3, None, 1]),
    build([3, 4, 5, 1, 3, None, 1])
]:
    print(main(root))
