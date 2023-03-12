def x(n):
    res = []
    quot = n
    while quot:
        res.append(quot % 10)
        quot //= 10
    res.reverse()
    return res


def y(n):
    res = 0
    quot = n
    while quot:
        res += quot % 10
        quot //= 10
    return res


def z(n):
    res = 0
    quot = n
    while quot:
        res = res * 10 + quot % 10
        quot //= 10
    return res


for n in [
    125, 47, 425, 59, 60, 150, 100
]:
    print(x(n), end=' ')
    print(y(n), end=' ')
    print(z(n))
