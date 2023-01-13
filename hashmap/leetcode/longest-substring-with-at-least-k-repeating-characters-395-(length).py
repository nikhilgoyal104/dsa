from collections import Counter


# T=n²,S=n
def x(s, k):
    def dfs(s):
        if len(s) < k:
            return 0
        res = 0
        for ch in set(s):
            if s.count(ch) < k:
                for part in s.split(ch):
                    res = max(res, dfs(part))
                return res
        return len(s)

    return dfs(s)


# T=n²,S=n
def y(s, k):
    def dfs(s):
        if len(s) < k:
            return 0
        for ch in set(s):
            if s.count(ch) < k:
                return max(dfs(part) for part in s.split(ch))
        return len(s)

    return dfs(s)


for s, k in [
    ('aaabb', 3),
    ('ababbc', 2),
    ('ababcabaaadc', 2)
]:
    print(x(s, k), end=' ')
    print(y(s, k))
