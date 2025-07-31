from util import build

inputs = [
    build([]),
    build([1]),
    build([1, 2]),
    build([1, 2, 3, 4, 5]),
]


def post(head):
    def dfs(head):
        if not head:
            return
        dfs(head.next)
        print(head.val, end=' ')

    return dfs(head)


def pre(head):
    def dfs(head):
        if not head:
            return
        print(head.val, end=' ')
        dfs(head.next)

    return dfs(head)


for head in inputs:
    post(head)
    print()

for head in inputs:
    pre(head)
    print()
