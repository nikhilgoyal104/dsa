class TrieNode:
    def __init__(self):
        self.word = False
        self.children = {}


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.word = True

    def getLastNodeInPrefix(self, word):
        node = self.root
        for char in word:
            node = node.children.get(char)
            if not node:
                return None
        return node

    def search(self, word):
        lastNodeInPrefix = self.getLastNodeInPrefix(word)
        return lastNodeInPrefix is not None and lastNodeInPrefix.word

    def startsWith(self, prefix):
        return self.getLastNodeInPrefix(prefix) is not None


trie = Trie()
for key in ['tri', 'try', 'their']:
    trie.insert(key)

print(trie.search('tri'))
print(trie.search('trim'))
