def p(x, n):
    if n < 0:
        n, x = -n, 1 / x

    def rec(n):
        if not n:
            return 1
        half = rec(n // 2)
        if n % 2:
            return x * half * half
        return half * half

    return rec(n)


for x, n in [
    (2.00000, 10),
    (2.10000, 3),
    (2.00000, -2)
]:
    print(p(x, n))
