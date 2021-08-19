def x(n):
    cols, diags, antidiags = set(), set(), set()

    def dfs(ri):
        if ri == n:
            return [[]]
        res = []
        for ci in range(n):
            if ci in cols or ri - ci in diags or ri + ci in antidiags:
                continue
            cols.add(ci)
            diags.add(ri - ci)
            antidiags.add(ri + ci)
            for path in dfs(ri + 1):
                res.append([(ri, ci)] + path)
            cols.remove(ci)
            diags.remove(ri - ci)
            antidiags.remove(ri + ci)
        return res

    return dfs(0)


def y(n):
    cols, diags, antidiags = set(), set(), set()

    def dfs(ri, path):
        if ri == n:
            print(path, end=' ')
            return
        for ci in range(n):
            if ci in cols or ri - ci in diags or ri + ci in antidiags:
                continue
            path.append((ri, ci))
            cols.add(ci)
            diags.add(ri - ci)
            antidiags.add(ri + ci)
            dfs(ri + 1, path)
            path.pop()
            cols.remove(ci)
            diags.remove(ri - ci)
            antidiags.remove(ri + ci)

    dfs(0, [])


for n in [4, 5]:
    print(x(n))
    y(n)
    print()
