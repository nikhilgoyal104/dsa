class TrieNode:
    def __init__(self):
        self.word = ''
        self.children = {}


class FileSystem:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word.split('/')[1:]:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        return node

    def search(self, word):
        node = self.root
        if word == '/':
            return node
        for char in word.split('/')[1:]:
            node = node.children[char]
        return node

    def ls(self, path):
        node = self.search(path)
        if node.word:
            return [path.split('/')[-1]]
        return sorted(node.children.keys())

    def mkdir(self, path):
        self.insert(path)

    def addContentToFile(self, filePath, content):
        self.insert(filePath).word += content

    def readContentFromFile(self, filePath):
        return self.search(filePath).word


fs = FileSystem()
print(fs.ls('/'))
print(fs.mkdir('/a/b/c'))
print(fs.addContentToFile('/a/b/c/d', 'hello'))
print(fs.ls('/'))
print(fs.readContentFromFile('/a/b/c/d'))
