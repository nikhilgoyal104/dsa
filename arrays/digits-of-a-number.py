def x(n):
    res, quot = [], n
    while quot:
        quot, rem = divmod(quot, 10)
        res.append(rem)
    res.reverse()
    return res


def y(n):
    res, quot = 0, n
    while quot:
        quot, rem = divmod(quot, 10)
        res += rem
    return res


def z(n):
    res, quot = 0, n
    while quot:
        quot, rem = divmod(quot, 10)
        res = res * 10 + rem
    return res


for n in [
    125, 47, 425, 59, 60, 150, 100
]:
    print(x(n), end=' ')
    print(y(n), end=' ')
    print(z(n))
