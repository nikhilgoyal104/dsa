# T=logn,S=1
def x(num):
    def dfs(num):
        if not num:
            return 0
        if num % 2:
            return 1 + dfs(num - 1)
        return 1 + dfs(num // 2)

    return dfs(num)


# T=logn,S=1
def y(num):
    res = 0
    while num:
        if num % 2:
            num -= 1
        else:
            num //= 2
        res += 1
    return res


for num in [
    14, 8, 123
]:
    print(x(num), end=' ')
    print(y(num))
