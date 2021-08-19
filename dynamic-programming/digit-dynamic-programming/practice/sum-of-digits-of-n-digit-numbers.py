def x(n):
    res = []
    for i in range(1, pow(10, n)):
        res.append(sum(int(d) for d in str(i)))
    return res


def y(n):
    def dfs(i, sum):
        if i == n:
            return [sum]
        res = []
        for digit in range(10):
            if not i and not digit:
                continue
            res += dfs(i + 1, sum + digit)
        return res

    return dfs(0, 0)


def z(n):
    def dfs(i):
        if i == n:
            return [0]
        res = []
        for digit in range(10):
            if not i and not digit:
                continue
            for path in dfs(i + 1):
                res.append(digit + path)
        return res

    return dfs(0)


for n in [2]:
    print(x(n))
    print(y(n))
    print(z(n))
