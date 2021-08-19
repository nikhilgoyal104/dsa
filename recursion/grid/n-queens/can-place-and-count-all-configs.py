def x(n):
    cols, diags, antidiags = set(), set(), set()

    def dfs(ri):
        if ri == n:
            return True
        for ci in range(n):
            if ci in cols or ri - ci in diags or ri + ci in antidiags:
                continue
            cols.add(ci)
            diags.add(ri - ci)
            antidiags.add(ri + ci)
            if dfs(ri + 1):
                return True
            cols.remove(ci)
            diags.remove(ri - ci)
            antidiags.remove(ri + ci)
        return False

    return dfs(0)


def y(n):
    cols, diags, antidiags = set(), set(), set()

    def dfs(ri):
        if ri == n:
            return 1
        count = 0
        for ci in range(n):
            if ci in cols or ri - ci in diags or ri + ci in antidiags:
                continue
            cols.add(ci)
            diags.add(ri - ci)
            antidiags.add(ri + ci)
            count += dfs(ri + 1)
            cols.remove(ci)
            diags.remove(ri - ci)
            antidiags.remove(ri + ci)
        return count

    return dfs(0)


for n in [1, 2, 3, 4, 5]:
    print(x(n), end=' ')
    print(y(n))
