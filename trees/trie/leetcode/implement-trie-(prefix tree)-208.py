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
            index = ord(char) - ord('a')
            if not node.children[index]:
                node.children[index] = TrieNode()
            node = node.children[index]
        node.word = True

    def searchPrefix(self, word):
        node = self.root
        for char in word:
            index = ord(char) - ord('a')
            if not node.children[index]:
                return None
            node = node.children[index]
        return node

    def search(self, word):
        node = self.searchPrefix(word)
        return node is not None and node.word

    def startsWith(self, prefix):
        return self.searchPrefix(prefix) is not None


keys = ['the', 'a', 'there', 'their']
trie = Trie()
for key in keys:
    trie.insert(key)

print(trie.search('the'))
print(trie.search('trim'))
print(trie.startsWith('xy'))
print(trie.startsWith('th'))
