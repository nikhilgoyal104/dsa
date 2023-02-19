from binarytree import Node as TreeNode


# T=n²,S=n
def main(n):
    cache = {0: 1}

    def dfs(n):
        if n in cache:
            return cache[n]
        cache[n] = 0
        for i in range(n):
            cache[n] += dfs(i) * dfs(n - 1 - i)
        return cache[n]

    return dfs(n)


for n in [
    1, 2, 3, 4, 19
]:
    print(main(n))
