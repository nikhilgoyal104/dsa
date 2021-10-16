class TrieNode:
    def __init__(self):
        self.isEnd = False
        self.children = [None] * 26


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for char in word:
            index = ord(char) - ord('a')
            if not curr.children[index]:
                curr.children[index] = TrieNode()
            curr = curr.children[index]
        curr.isEnd = True

    def searchPrefix(self, word):
        curr = self.root
        for char in word:
            index = ord(char) - ord('a')
            if not curr.children[index]:
                return None
            curr = curr.children[index]
        return curr

    def search(self, word):
        node = self.searchPrefix(word)
        return node and node.isEnd

    def startsWith(self, prefix):
        return self.searchPrefix(prefix) is not None


keys = ['the', 'a', 'there', 'their']
trie = Trie()
for key in keys:
    trie.insert(key)
