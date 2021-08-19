# T=n!,S=n²
def x(n):
    cols, diags, antidiags = set(), set(), set()

    def choose(ri, ci):
        cols.add(ci)
        diags.add(ri - ci)
        antidiags.add(ri + ci)

    def discard(ri, ci):
        cols.remove(ci)
        diags.remove(ri - ci)
        antidiags.remove(ri + ci)

    def dfs(ri):
        if ri == n:
            return 1
        count = 0
        for ci in range(n):
            if ci in cols or ri - ci in diags or ri + ci in antidiags:
                continue
            choose(ri, ci)
            count += dfs(ri + 1)
            discard(ri, ci)
        return count

    return dfs(0)


for n in [1, 2, 3, 4, 5]:
    print(x(n))
