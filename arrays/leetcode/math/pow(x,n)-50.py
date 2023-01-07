def main(x, n):
    if n < 0:
        n, x = -n, 1 / x

    def dfs(n):
        if not n:
            return 1
        subproblem = dfs(n // 2)
        if n % 2 == 1:
            return x * subproblem * subproblem
        return subproblem * subproblem

    return dfs(n)


for x, n in [
    (2.00000, 10),
    (2.10000, 3),
    (2.00000, -2)
]:
    print(main(x, n))
