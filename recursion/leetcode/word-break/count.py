# T=n²+2ⁿ+w,S=2ⁿnw
def x(s, words):
    def dfs(s):
        if not s:
            return 1
        res = 0
        for word in words:
            if s.startswith(word):
                res += dfs(s[len(word):])
        return res

    return dfs(s)


# T=n²+2ⁿ+w,S=2ⁿnw
def y(s, words):
    words = set(words)

    def dfs(s):
        if not s:
            return 1
        res = 0
        for i in range(len(s)):
            prefix, suffix = s[:i + 1], s[i + 1:]
            if prefix in words:
                res += dfs(suffix)
        return res

    return dfs(s)


# T=n²+2ⁿ+w,S=2ⁿnw
def z(s, words):
    words = set(words)
    cache = {'': 1}

    def dfs(s):
        if s in cache:
            return cache[s]
        cache[s] = 0
        for i in range(len(s)):
            prefix, suffix = s[:i + 1], s[i + 1:]
            if prefix in words:
                cache[s] += dfs(suffix)
        return cache[s]

    return dfs(s)


for s, words in [
    ('nikhil', ['nikhil']),
    ('catsanddog', ['cat', 'cats', 'and', 'sand', 'dog']),
    ('pineapplepenapple', ['apple', 'pen', 'applepen', 'pine', 'pineapple']),
    ('catsandog', ['cats', 'dog', 'sand', 'and', 'cat']),
]:
    print(x(s, words), end=' ')
    print(y(s, words), end=' ')
    print(z(s, words))
