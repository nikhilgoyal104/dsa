# T=mn
def x(s1, s2, s3):
    m, n, o, dp = len(s1), len(s2), len(s3), {}
    if m + n != o:
        return False

    def dfs(i, j, k):
        if i + j == m + n:
            return True
        key = i, j
        if key in dp:
            return dp[key]
        dp[key] = False
        if i < m and s1[i] == s3[k]:
            dp[key] = dfs(i + 1, j, k + 1)
        elif j < n and s2[j] == s3[k]:
            dp[key] = dfs(i, j + 1, k + 1)
        elif i < m and j < n and s1[i] == s2[j] == s3[k]:
            dp[key] = dfs(i + 1, j, k + 1) or dfs(i, j + 1, k + 1)
        return dp[key]

    return dfs(0, 0, 0)


for s1, s2, s3 in [
    (
            'aabcc',
            'dbbca',
            'aadbbcbcac'
    ),
    (
            'aabcc',
            'dbbca',
            'aadbbbaccc'
    ),
    (
            '',
            '',
            ''
    ),
    (
            '',
            '',
            'a'
    ),
    (
            'a',
            'b',
            'a',
    ),
    (
            'aabd',
            'abdc',
            'aabdbadc'
    ),
    (
            'bbbbbabbbbabaababaaaabbababbaaabbabbaaabaaaaababbbababbbbbabbbbababbabaabababbbaabababababbbaaababaa',
            'babaaaabbababbbabbbbaabaabbaabbbbaabaaabaababaaaabaaabbaaabaaaabaabaabbbbbbbbbbbabaaabbababbabbabaab',
            'babbbabbbaaabbababbbbababaabbabaabaaabbbbabbbaaabbbaaaaabbbbaabbaaabababbaaaaaabababbababaababbababbbababbbbaaaabaabbabbaaaaabbabbaaaabbbaabaaabaababaababbaaabbbbbabbbbaabbabaabbbbabaaabbababbabbabbab'
    )
]:
    print(x(s1, s2, s3))
