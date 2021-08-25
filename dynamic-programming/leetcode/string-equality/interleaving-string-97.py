# T=mn
def x(s1, s2, s3):
    m, n, o, dp = len(s1), len(s2), len(s3), {}
    if m + n != o:
        return False

    def dfs(i, j, k):
        if i == m and j == n:
            return True
        key = i, j
        if key in dp:
            return dp[key]
        f1 = f2 = False
        if i < m and s1[i] == s3[k]:
            f1 = dfs(i + 1, j, k + 1)
        if j < n and s2[j] == s3[k]:
            f2 = dfs(i, j + 1, k + 1)
        dp[key] = f1 or f2
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
