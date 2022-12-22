# T=n²+2ⁿ+w,S=2ⁿnw
def x(s, words):
    def dfs(s):
        if not s:
            return 1
        count = 0
        for word in words:
            if s.startswith(word):
                count += dfs(s[len(word):])
        return count

    return dfs(s)


# T=n²+2ⁿ+w,S=2ⁿnw
def y(s, words):
    words = set(words)

    def dfs(s):
        if not s:
            return 1
        count = 0
        for i in range(len(s)):
            prefix, suffix = s[:i + 1], s[i + 1:]
            if prefix in words:
                count += dfs(suffix)
        return count

    return dfs(s)


# T=n²+2ⁿ+w,S=2ⁿnw
def z(s, words):
    words = set(words)
    dp = {'': 1}

    def dfs(s):
        if s in dp:
            return dp[s]
        dp[s] = 0
        for i in range(len(s)):
            prefix, suffix = s[:i + 1], s[i + 1:]
            if prefix in words:
                dp[s] += dfs(suffix)
        return dp[s]

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
