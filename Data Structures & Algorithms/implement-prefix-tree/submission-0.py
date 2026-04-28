class TriNode:
    def __init__(self, value: str):
        self.value = value
        self.children = {}
        self.end = False

class PrefixTree:

    def __init__(self):
        self.root = TriNode("")

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TriNode(c)
            curr = curr.children[c]
        curr.end = True


    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.end
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True
        
        