def isPalindrome(s):
    return s == s[::-1]


# T=n2ⁿ,S=n
def x(s):
    res, path = [], []

    def dfs(s):
        if not s:
            res.append(path[:])
            return
        for i in range(len(s)):
            prefix, suffix = s[:i + 1], s[i + 1:]
            if isPalindrome(prefix):
                path.append(prefix)
                dfs(suffix)
                path.pop()

    dfs(s)
    return res


# T=n2ⁿ,S=n
def y(s):
    def dfs(s):
        if not s:
            return [[]]
        res = []
        for i in range(len(s)):
            prefix, suffix = s[:i + 1], s[i + 1:]
            if isPalindrome(prefix):
                for path in dfs(suffix):
                    res.append([prefix] + path)
        return res

    return dfs(s)


# T=n2ⁿ,S=n²
def z(s):
    cache = {'': [[]]}

    def dfs(s):
        if s in cache:
            return cache[s]
        cache[s] = []
        for i in range(len(s)):
            prefix, suffix = s[:i + 1], s[i + 1:]
            if isPalindrome(prefix):
                for path in dfs(suffix):
                    cache[s].append([prefix] + path)
        return cache[s]

    return dfs(s)


for s in [
    'abaaba',
    'nitin',
    'geeks',
    'aab',
    'aaa',
    'a'
]:
    print(x(s))
    print(y(s))
    print(z(s))
    print()
