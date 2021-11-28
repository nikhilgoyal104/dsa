def isPalindrome(s):
    return s == s[::-1]


def main(s):
    def dfs(s):
        if not s:
            return True
        for i in range(len(s)):
            prefix, suffix = s[:i + 1], s[i + 1:]
            if isPalindrome(prefix) and dfs(suffix):
                return True
        return False

    return dfs(s)


for s in [
    'nitin',
    'geeks',
    'aab',
    'a'
]:
    print(main(s))
