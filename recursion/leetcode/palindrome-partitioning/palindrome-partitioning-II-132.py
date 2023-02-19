from math import inf


def isPalindrome(s):
    return s == s[::-1]


# T=n2ⁿ,S=n
def x(s):
    def dfs(s):
        if not s:
            return -1
        res = inf
        for i in range(len(s)):
            prefix, suffix = s[:i + 1], s[i + 1:]
            if isPalindrome(prefix):
                res = min(res, 1 + dfs(suffix))
        return res

    return dfs(s)


# T=n²n,S=n
def y(s):
    cache = {'': -1}

    def dfs(s):
        if s in cache:
            return cache[s]
        cache[s] = inf
        for i in range(len(s)):
            prefix, suffix = s[:i + 1], s[i + 1:]
            if isPalindrome(prefix):
                cache[s] = min(cache[s], 1 + dfs(suffix))
        return cache[s]

    return dfs(s)


for s in [
    'aab',
    'a',
    'ab',
    'nitin',
    'geeks'
]:
    print(x(s), end=' ')
    print(y(s))
