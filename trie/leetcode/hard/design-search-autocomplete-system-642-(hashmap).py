class TrieNode:
    def __init__(self):
        self.count = 0
        self.children = {}


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, sentence, count):
        node = self.root
        for char in sentence:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.count += count

    def getLastNodeInPrefix(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return None
            node = node.children[char]
        return node

    def content(self, root, start):
        res = []

        def dfs(root, path):
            if root.count:
                res.append((root.count, path))
            for child in root.children:
                dfs(root.children[child], path + child)

        dfs(root, start)
        return res

    def getSentencesStartingWithPrefix(self, prefix):
        lastNodeInPrefix = self.getLastNodeInPrefix(prefix)
        if not lastNodeInPrefix:
            return []
        return self.content(lastNodeInPrefix, prefix)


class AutocompleteSystem:

    def __init__(self, sentences, times):
        self.trie = Trie()
        for sentence, count in zip(sentences, times):
            self.trie.insert(sentence, count)
        self.current = ''

    def input(self, c):
        if c == '#':
            self.trie.insert(self.current, 1)
            self.current = ''
            return []
        self.current += c
        data = self.trie.getSentencesStartingWithPrefix(self.current)
        data = sorted(data, key=lambda x: (-x[0], x[1]))[:3]
        return [sentence for _, sentence in data]


testcases = [
    ['i', ' ', 'a', '#'],
    ['i', ' ', 'a', '#', 'i', ' ', 'a', '#', 'i', ' ', 'a', '#'],
]

for testcase in testcases:
    autocomplete = AutocompleteSystem(
        ['i love you', 'island', 'ironman', 'i love leetcode'],
        [5, 3, 2, 2]
    )
    for prefix in testcase:
        print(autocomplete.input(prefix))
    print()
