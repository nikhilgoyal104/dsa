# T=n²+2ⁿ+w,S=2ⁿnw
def x(s, words):
    def dfs(s):
        if not s:
            return True
        for word in words:
            if s.startswith(word) and dfs(s[len(word):]):
                return True
        return False

    return dfs(s)


# T=n²+2ⁿ+w,S=2ⁿnw
def y(s, words):
    words = set(words)

    def dfs(s):
        if not s:
            return True
        for i in range(len(s)):
            prefix, suffix = s[:i + 1], s[i + 1:]
            if prefix in words and dfs(suffix):
                return True
        return False

    return dfs(s)


for s, words in [
    ('nikhil', ['nikhil']),
    ('catsanddog', ['cat', 'cats', 'and', 'sand', 'dog']),
    ('pineapplepenapple', ['apple', 'pen', 'applepen', 'pine', 'pineapple']),
    ('catsandog', ['cats', 'dog', 'sand', 'and', 'cat']),
]:
    print(x(s, words), end=' ')
    print(y(s, words))
