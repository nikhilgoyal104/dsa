def construct():
    decoder, char = {}, 'a'
    for i in range(1, 27):
        decoder[str(i)] = char
        char = chr(ord(char) + 1)
    return decoder


# T=n,S=n
def main(s):
    cache = {'': ['']}
    decoder = construct()

    def dfs(s):
        if s in cache:
            return cache[s]
        if s[0] == '0':
            return []
        cache[s] = []
        for path in dfs(s[1:]):
            cache[s].append(decoder[s[:1]] + path)
        if len(s) >= 2 and int(s[:2]) <= 26:
            for path in dfs(s[2:]):
                cache[s].append(decoder[s[:2]] + path)
        return cache[s]

    return dfs(s)


for s in [
    '12', '123', '226', '0', '06', '27', '1201234'
]:
    print(main(s))
