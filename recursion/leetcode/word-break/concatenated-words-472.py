# T=n³w
def main(words):
    def dfs(s, prewords, dp):
        if s in dp:
            return dp[s]
        dp[s] = False
        for i in range(1, len(s) + 1):
            prefix, suffix = s[:i], s[i:]
            if prefix in prewords and dfs(suffix, prewords, dp):
                dp[s] = True
                return dp[s]
        return dp[s]

    words.sort(key=len)
    res, prewords = [], set()
    for word in words:
        if word and dfs(word, prewords, {'': True}):
            res.append(word)
        prewords.add(word)
    return res


for words in [
    ['cat', 'cats', 'catsdogcats', 'dog', 'dogcatsdog', 'hippopotamuses', 'rat', 'ratcatdogcat'],
    ['cat', 'dog', 'catdog'],
    ['']
]:
    print(main(words))
