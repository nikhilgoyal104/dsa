# T=n³,S=n
def x(s, words):
    dp = {'': True}

    def dfs(s):
        if s in dp:
            return dp[s]
        dp[s] = False
        for word in words:
            if s.startswith(word) and dfs(s[len(word):]):
                dp[s] = True
                return dp[s]
        return dp[s]

    return dfs(s)


# T=n³,S=n
def y(s, words):
    n, words = len(s), set(words)
    dp = {'': True}

    def dfs(s):
        if s in dp:
            return dp[s]
        dp[s] = False
        for i in range(len(s)):
            prefix, suffix = s[:i + 1], s[i + 1:]
            if prefix in words and dfs(suffix):
                dp[s] = True
                return dp[s]
        return dp[s]

    return dfs(s)


# T=n³,S=n
def z(s, words):
    n, words = len(s), set(words)
    dp = {n: True}

    def dfs(start):
        if start in dp:
            return dp[start]
        dp[start] = False
        for end in range(start + 1, n + 1):
            if s[start:end] in words and dfs(end):
                dp[start] = True
                return dp[start]
        return dp[start]

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
