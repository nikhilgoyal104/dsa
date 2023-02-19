# T=n³,S=n
def x(s, words):
    cache = {'': True}

    def dfs(s):
        if s in cache:
            return cache[s]
        cache[s] = False
        for word in words:
            if s.startswith(word) and dfs(s[len(word):]):
                cache[s] = True
                return cache[s]
        return cache[s]

    return dfs(s)


# T=n³,S=n
def y(s, words):
    n, words = len(s), set(words)
    cache = {'': True}

    def dfs(s):
        if s in cache:
            return cache[s]
        cache[s] = False
        for i in range(len(s)):
            prefix, suffix = s[:i + 1], s[i + 1:]
            if prefix in words and dfs(suffix):
                cache[s] = True
                return cache[s]
        return cache[s]

    return dfs(s)


# T=n³,S=n
def z(s, words):
    n, words = len(s), set(words)
    cache = {n: True}

    def dfs(start):
        if start in cache:
            return cache[start]
        cache[start] = False
        for end in range(start + 1, n + 1):
            if s[start:end] in words and dfs(end):
                cache[start] = True
                return cache[start]
        return cache[start]

    return dfs(0)


for s, words in [
    ('leetcode', ['leet', 'code']),
    ('applepenapple', ['apple', 'pen']),
    ('catsandog', ['cats', 'dog', 'sand', 'and', 'cat']),
    (
            'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab',
            ['a', 'aa', 'aaa', 'aaaa', 'aaaaa', 'aaaaaa', 'aaaaaaa', 'aaaaaaaa', 'aaaaaaaaa', 'aaaaaaaaaa']
    )
]:
    print(x(s, words), end=' ')
    print(y(s, words), end=' ')
    print(z(s, words))
