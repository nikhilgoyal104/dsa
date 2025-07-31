from util import build


# T=n,S=n
def main(head):
    def dfs(head):
        if not head:
            return
        dfs(head.next)
        print(head.val, end=' ')

    return dfs(head)


for head in [
    build([]),
    build([1]),
    build([1, 2]),
    build([1, 2, 3, 4, 5]),
]:
    print(main(head))
