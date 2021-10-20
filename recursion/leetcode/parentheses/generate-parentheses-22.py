def main(n):
    res = []

    def dfs(open, close, path):
        if open == close == n:
            res.append(path)
            return
        if open < n:
            dfs(open + 1, close, path + '(')
        if close < open:
            dfs(open, close + 1, path + ')')

    dfs(0, 0, '')
    return res


for n in [1, 2, 3]:
    print(main(n))
