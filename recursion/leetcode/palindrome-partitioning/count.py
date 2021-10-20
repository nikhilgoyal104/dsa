def isPalindrome(s):
    return s == s[::-1]


def main(s):
    def dfs(s):
        if not s:
            return 1
        res = 0
        for i in range(len(s)):
            prefix, suffix = s[:i + 1], s[i + 1:]
            if isPalindrome(prefix):
                res += dfs(suffix)
        return res

    return dfs(s)


for s in [
    'abaaba',
    'nitin',
    'geeks',
    'aab',
    'aaa',
    'a'
]:
    print(main(s))
