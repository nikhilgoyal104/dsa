from binarytree import Node as TreeNode


def main(n):
    def dfs(start, end):
        if start > end:
            return [None]
        res = []
        for i in range(start, end + 1):
            for lst in dfs(start, i - 1):
                for rst in dfs(i + 1, end):
                    res.append(TreeNode(i, lst, rst))
        return res

    return dfs(1, n)


for n in [
    1, 3
]:
    for root in main(n):
        print(root)
