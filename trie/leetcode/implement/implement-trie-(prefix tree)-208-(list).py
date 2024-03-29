class TrieNode:
    def __init__(self):
        self.word = False
        self.children = [None] * 26


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            index = ord(char) - 97
            if not node.children[index]:
                node.children[index] = TrieNode()
            node = node.children[index]
        node.word = True

    def _getLastNodeInPrefix(self, prefix):
        node = self.root
        for char in prefix:
            index = ord(char) - 97
            if not node.children[index]:
                return None
            node = node.children[index]
        return node

    def search(self, word):
        lastNodeInPrefix = self._getLastNodeInPrefix(word)
        return lastNodeInPrefix is not None and lastNodeInPrefix.word

    def startsWith(self, prefix):
        lastNodeInPrefix = self._getLastNodeInPrefix(prefix)
        return lastNodeInPrefix is not None


keys = ['the', 'a', 'there', 'their']
trie = Trie()
for key in keys:
    trie.insert(key)

print(trie.search('the'))
print(trie.search('trim'))
print(trie.startsWith('xy'))
print(trie.startsWith('th'))
