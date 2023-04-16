from generic.util import build


def main(root):
    def dfs(root):
        print(root.val, end=' ')
        for child in root.children:
            dfs(child)

    dfs(root)


root = build([1, 2, 5, -1, 6, -1, -1, 3, 7, -1, 8, 11, -1, 12, -1, -1, 9, -1, -1, 4, 10, -1, -1, -1])
main(root)
