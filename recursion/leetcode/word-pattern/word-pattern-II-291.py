def main(pattern, s):
    map, vis = {}, set()

    def dfs(pattern, s):
        if not pattern and not s:
            return True
        if not pattern or not s:
            return False
        letter = pattern[0]
        if letter in map:
            return s.startswith(map[letter]) and dfs(pattern[1:], s[len(map[letter]):])
        for i in range(len(s)):
            prefix, suffix = s[:i + 1], s[i + 1:]
            if prefix in vis:
                continue
            vis.add(prefix)
            map[letter] = prefix
            if dfs(pattern[1:], suffix):
                return True
            del map[letter]
            vis.remove(prefix)
        return False

    return dfs(pattern, s)


for pattern, s in [
    ('ab', 'aa'),
    ('sucks', 'teezmnoteez'),
    ('pep', 'treegraphtree'),
    ('abab', 'redblueredblue'),
    ('aaaa', 'asdasdasdasd'),
    ('abab', 'asdasdasdasd'),
    ('aabb', 'xyzabcxzyabc'),
    ('abba', 'dogdogdogdog')
]:
    print(main(pattern, s))
