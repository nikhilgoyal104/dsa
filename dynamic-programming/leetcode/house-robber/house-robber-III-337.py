from binarytree import build2


# T=n,S=n
def main(root):
    cache = {None: 0}

    def dfs(root):
        if root in cache:
            return cache[root]
        inc = root.val
        exc = 0
        for child in [root.left, root.right]:
            if child:
                inc += dfs(child.left) + dfs(child.right)
            exc += dfs(child)
        cache[root] = max(inc, exc)
        return cache[root]

    return dfs(root)


for root in [
    build2([3, 2, 3, None, 3, None, 1]),
    build2([3, 4, 5, 1, 3, None, 1])
]:
    print(main(root))
