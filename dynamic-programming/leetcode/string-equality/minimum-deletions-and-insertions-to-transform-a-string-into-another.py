def x(s1, s2):
    def dfs(s1, s2):
        if not s2:
            return len(s1)
        if not s1:
            return len(s2)
        if s1[0] != s2[0]:
            return 1 + min(dfs(s1[1:], s2), dfs(s1, s2[1:]))
        return dfs(s1[1:], s2[1:])

    return dfs(s1, s2)


def y(s1, s2):
    m, n = len(s1), len(s2)

    def lcs(s1, s2):
        return 1

    lcs = lcs(s1, s2)
    minInsertions, minDeletions = m - lcs, n - lcs
    print(minInsertions, minDeletions)


for s1, s2 in [
    ('abc', 'fbc'),
    ('abdca', 'cbda'),
    ('passport', 'ppsspt')
]:
    print(x(s1, s2))
