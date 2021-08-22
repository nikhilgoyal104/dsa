def clean(p):
    i, n, res = 0, len(p), []
    while i < n:
        res.append(p[i])
        while i + 1 < n and p[i] == p[i + 1] == '*':
            i += 1
        i += 1
    return ''.join(res)


# T=sp(s+p),S=sp
# s+p time to create a hash of tuple s,p the first time
# min(s,p) time for the string equality check
# s+p time to create s[1:] and p[1:]
def x(s, p):
    dp = {}

    def dfs(s, p):
        if s == p or p == '*':
            return True
        if not s or not p:
            return False
        key = s, p
        if key in dp:
            return dp[key]
        if p[0] in {s[0], '?'}:
            dp[key] = dfs(s[1:], p[1:])
            return dp[key]
        if p[0] == '*':
            for i in range(len(s) + 1):
                if dfs(s[i:], p[1:]):
                    dp[key] = True
                    return dp[key]
        return False

    return dfs(s, clean(p))


for s, p in [
    ('aa', 'a'),
    ('aa', '*'),
    ('cb', '?a'),
    ('adceb', '*a*b'),
    ('acdcb', 'a*c?b'),
    ('', '******'),
    ('abcd', '******'),
    ('aaabbbaabaaaaababaabaaabbabbbbbbbbaabababbabbbaaaaba', 'a*******b'),
    (
            'baaaababbbaabbbbabbababaababaaabaababbbaabaabbbbaabbbbbbaabaabbababaaaaaaaabbbaaabbbababbbbbabbbbabbbbabbaabaababababbbababbbbbbbaaaaabbbbabbbbbaabbbaaaabaaabbabbabaabbbbabbbabbbaababbabbaaaababbababa',
            '*bb*abb*a**ba**aba*b*bbb*abbaaa*bb*b**a*b*b**a**abb***ab*b**b*b*a******a*a*babaa*bab*a*b****bb*babb*baa'
    ),
    (
            'bbbbaaaaabaabbbbaabaaabaabbababbbaaabbababbbabaabaabaabababaaabaaaabbaabbaabbaaaaabbabbbbaaaababbaaaabbabbbaabaaabbaabaabaaababbabbaababaababbbbbaabbabbabbbbaabbaaababbabaaabbbbbbbbaababbbbbbabbaabaaa',
            'b*a**b***abaabaaaba*abaaaaabaabb*bbb*aa*ab*a**b**b*a**a**a*abbb***bb*b*****baababaa**ab*aa*bbaba**bb*b*'
    ),
    (
            'abbbbaaaabbabaabaabbbababaaabaabaaabaababbaabababababaaaababbbabbabbaabbbaababbbaabbbabbbababbaaabbabaabaaabbbabbaaaaaababbbabbaaabaabbbbbaaaaabaaaaaababbbbaaababbbaaabbabbababaabaabbbaababbbbaaaaaabbaaab',
            '*ba**b*a****a*bb*a*b***bbab*bbb**bb****b*b**aaa*b*babab*b*b*a*b***abb**aa**a*****a**bb****a*bb*a***ababb'
    )
]:
    print(x(s, p))
