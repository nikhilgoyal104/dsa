# T=n³w
def main(words):
    words.sort(key=len)
    res = []
    prewords = set()

    def dfs(s, prewords, cache):
        if s in cache:
            return cache[s]
        cache[s] = False
        for i in range(len(s)):
            prefix, suffix = s[:i + 1], s[i + 1:]
            if prefix in prewords and dfs(suffix, prewords, cache):
                cache[s] = True
                return cache[s]
        return cache[s]

    for word in words:
        if not word:
            continue
        if dfs(word, prewords, {'': True}):
            res.append(word)
        prewords.add(word)
    return res


for words in [
    ['cat', 'cats', 'catsdogcats', 'dog', 'dogcatsdog', 'hippopotamuses', 'rat', 'ratcatdogcat'],
    ['cat', 'dog', 'catdog'],
    ['']
]:
    print(main(words))
