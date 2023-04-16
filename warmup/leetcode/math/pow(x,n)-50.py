inputs = [
    (2.00000, 10),
    (2.10000, 3),
    (2.00000, -2)
]


# T=n,S=n
def main(x, n):
    if n < 0:
        n = -n
        x = 1 / x

    def dfs(n):
        if not n:
            return 1
        return x * dfs(n - 1)

    return dfs(n)


for x, n in inputs:
    print(main(x, n), end=' ')

print()


# T=n,S=n
def main(x, n):
    if n < 0:
        n = -n
        x = 1 / x

    def dfs(n):
        if not n:
            return 1
        if n % 2 == 1:
            return x * dfs(n // 2) * dfs(n // 2)
        return dfs(n // 2) * dfs(n // 2)

    return dfs(n)


for x, n in inputs:
    print(main(x, n), end=' ')

print()


# T=logn,S=logn
def main(x, n):
    if n < 0:
        n = -n
        x = 1 / x

    def dfs(n):
        if not n:
            return 1
        subproblem = dfs(n // 2)
        if n % 2 == 1:
            return x * subproblem * subproblem
        return subproblem * subproblem

    return dfs(n)


for x, n in inputs:
    print(main(x, n), end=' ')
