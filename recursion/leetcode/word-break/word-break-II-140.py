# T=n²+2ⁿ+w,S=2ⁿnw
def x(s, words):
    cache = {'': ['']}

    def dfs(s):
        if s in cache:
            return cache[s]
        cache[s] = []
        for word in words:
            if s.startswith(word):
                for path in dfs(s[len(word):]):
                    cache[s].append(word + (' ' + path if path else path))
        return cache[s]

    return dfs(s)


# T=n²+2ⁿ+w,S=2ⁿnw
def y(s, words):
    cache = {'': ['']}
    words = set(words)

    def dfs(s):
        if s in cache:
            return cache[s]
        cache[s] = []
        for i in range(len(s)):
            prefix, suffix = s[:i + 1], s[i + 1:]
            if prefix in words:
                for path in dfs(suffix):
                    cache[s].append((prefix + ' ' + path).rstrip())
        return cache[s]

    return dfs(s)


for s, words in [
    ('nikhil', ['nikhil']),
    ('catsanddog', ['cat', 'cats', 'and', 'sand', 'dog']),
    ('pineapplepenapple', ['apple', 'pen', 'applepen', 'pine', 'pineapple']),
    ('catsandog', ['cats', 'dog', 'sand', 'and', 'cat']),
]:
    print(x(s, words), end=' ')
    print(y(s, words))
