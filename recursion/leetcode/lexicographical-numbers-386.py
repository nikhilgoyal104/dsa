# T=nlogn,S=1
def x(n):
    return list(map(int, sorted(str(val) for val in range(1, n + 1))))


# T=n,S=1
def y(n):
    res = []

    def dfs(num):
        if num > n:
            return
        res.append(num)
        for digit in range(10):
            dfs(10 * num + digit)

    for num in range(1, 10):
        dfs(num)
    return res


for n in [
    2, 13, 24
]:
    print(x(n))
    print(y(n))
