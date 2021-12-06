from collections import defaultdict, deque


def construct(wordList):
    n = len(wordList[0])
    graph = defaultdict(set)
    for word in wordList:
        for i in range(n):
            graph[word[:i] + '*' + word[i + 1:]].add(word)
    return graph


# L=length of each word,N=length of list
# T=NL²26,S=NL²
def main(beginWord, endWord, wordList):
    n = len(beginWord)
    wordList.append(beginWord)
    graph = construct(wordList)
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


for beginWord, endWord, wordList in [
    ('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log', 'cog']),
    ('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log']),
    ('hot', 'dog', ['hot', 'dog']),
]:
    print(main(beginWord, endWord, wordList))
