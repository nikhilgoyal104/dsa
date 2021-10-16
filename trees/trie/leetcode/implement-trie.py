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

    def searchPrefix(self, word):
        node = self.root
        for char in word:
            node = node.children.get(char)
            if not node:
                return None
        return node

    def search(self, word):
        node = self.searchPrefix(word)
        return node is not None and node.word

    def startsWith(self, prefix):
        return self.searchPrefix(prefix) is not None


trie = Trie()
for key in ['tri', 'try', 'their']:
    trie.insert(key)

print(trie.search('tri'))
print(trie.search('trim'))
