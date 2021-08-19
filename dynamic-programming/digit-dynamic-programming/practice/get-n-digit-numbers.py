def x(n):
    def dfs(i, num):
        if i == n:
            return [num]
        res = []
        for digit in range(10):
            if not i and not digit:
                continue
            res += dfs(i + 1, num * 10 + digit)
        return res

    return dfs(0, 0)


def y(n):
    def dfs(i):
        if i == n:
            return [0]
        res = []
        for digit in range(10):
            if not i and not digit:
                continue
            for num in dfs(i + 1):
                res.append(digit * pow(10, n - 1 - i) + num)
        return res

    return dfs(0)


for n in [2]:
    print(x(n))
    print(y(n))
