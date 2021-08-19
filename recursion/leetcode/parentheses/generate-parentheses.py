def v(n):
    def dfs(n):
        if not n:
            return ['']
        res = []
        for path in dfs(n - 1):
            for i in range(len(path) + 1):
                res.append(path[:i] + '()' + path[i:])
        return list(set(res))

    return dfs(n)


def valid(path):
    bal = 0
    for char in path:
        bal += 1 if char == '(' else -1
        if bal < 0:
            return False
    return not bal


def w(n):
    res = []

    def dfs(path):
        if len(path) == 2 * n:
            if valid(path):
                res.append(''.join(path))
            return
        path.append('(')
        dfs(path)
        path.pop()
        path.append(')')
        dfs(path)
        path.pop()

    dfs([])
    return res


def x(n):
    res = []

    def dfs(path):
        if len(path) == 2 * n:
            if valid(path):
                res.append(path)
            return
        dfs(path + '(')
        dfs(path + ')')

    dfs('')
    return res


def y(n):
    def dfs(i):
        if i == 2 * n:
            return ['']
        res = []
        for path in dfs(i + 1):
            res.append('(' + path)
        for path in dfs(i + 1):
            res.append(')' + path)
        return res

    return [path for path in dfs(0) if valid(path)]


def z(n):
    def dfs(path):
        if len(path) == 2 * n:
            return [path] if valid(path) else []
        res = []
        res += dfs(path + '(')
        res += dfs(path + ')')
        return res

    return dfs('')


for n in [1, 2, 3]:
    print(v(n), end=' ')
    print(w(n), end=' ')
    print(x(n), end=' ')
    print(y(n), end=' ')
    print(z(n))
