# T=n²+2ⁿ+w,S=2ⁿnw
def x(s, words):
    dp = {'': ['']}

    def dfs(s):
        if s in dp:
            return dp[s]
        dp[s] = []
        for word in words:
            if s.startswith(word):
                for path in dfs(s[len(word):]):
                    dp[s].append(word + (' ' + path if path else path))
        return dp[s]

    return dfs(s)


# T=n²+2ⁿ+w,S=2ⁿnw
def y(s, words):
    words, dp = set(words), {'': ['']}

    def dfs(s):
        if s in dp:
            return dp[s]
        dp[s] = []
        for i in range(len(s)):
            prefix, suffix = s[:i + 1], s[i + 1:]
            if prefix in words:
                for path in dfs(suffix):
                    dp[s].append((prefix + ' ' + path).rstrip())
        return dp[s]

    return dfs(s)


for s, words in [
    ('nikhil', ['nikhil']),
    ('catsanddog', ['cat', 'cats', 'and', 'sand', 'dog']),
    ('pineapplepenapple', ['apple', 'pen', 'applepen', 'pine', 'pineapple']),
    ('catsandog', ['cats', 'dog', 'sand', 'and', 'cat']),
]:
    print(x(s, words), end=' ')
    print(y(s, words))
