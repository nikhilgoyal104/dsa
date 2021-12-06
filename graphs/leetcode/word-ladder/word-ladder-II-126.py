from collections import defaultdict, deque


def construct(wordList):
    n = len(wordList[0])
    graph = defaultdict(set)
    for word in wordList:
        for i in range(n):
            graph[word[:i] + '*' + word[i + 1:]].add(word)
    return graph


def getSize(graph, beginWord, endWord):
    n = len(beginWord)
    queue, vis = deque([(beginWord, 1)]), set()
    while queue:
        src, dist = queue.popleft()
        if src == endWord:
            return dist
        for i in range(n):
            for nbr in graph[src[:i] + '*' + src[i + 1:]]:
                if nbr not in vis:
                    vis.add(nbr)
                    queue.append((nbr, dist + 1))
    return 0


def main(beginWord, endWord, wordList):
    n = len(beginWord)
    wordList.append(beginWord)
    graph = construct(wordList)
    size = getSize(graph, beginWord, endWord)
    vis = set()

    def dfs(src, level):
        if src == endWord:
            return [[src]]
        vis.add(src)
        res = []
        for i in range(n):
            for nbr in graph[src[:i] + '*' + src[i + 1:]]:
                if nbr not in vis and level < size:
                    for path in dfs(nbr, level + 1):
                        res.append([src] + path)
        vis.remove(src)
        return res

    return dfs(beginWord, 1)


for beginWord, endWord, wordList in [
    ('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log', 'cog']),
    ('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log']),
    ('qa', 'sq',
     ['si', 'go', 'se', 'cm', 'so', 'ph', 'mt', 'db', 'mb', 'sb', 'kr', 'ln', 'tm', 'le', 'av', 'sm', 'ar', 'ci', 'ca',
      'br', 'ti', 'ba', 'to', 'ra', 'fa', 'yo', 'ow', 'sn', 'ya', 'cr', 'po', 'fe', 'ho', 'ma', 're', 'or', 'rn', 'au',
      'ur', 'rh', 'sr', 'tc', 'lt', 'lo', 'as', 'fr', 'nb', 'yb', 'if', 'pb', 'ge', 'th', 'pm', 'rb', 'sh', 'co', 'ga',
      'li', 'ha', 'hz', 'no', 'bi', 'di', 'hi', 'qa', 'pi', 'os', 'uh', 'wm', 'an', 'me', 'mo', 'na', 'la', 'st', 'er',
      'sc', 'ne', 'mn', 'mi', 'am', 'ex', 'pt', 'io', 'be', 'fm', 'ta', 'tb', 'ni', 'mr', 'pa', 'he', 'lr', 'sq',
      'ye'])
]:
    print(main(beginWord, endWord, wordList))
