class Node:
    def __init__(self, n):
        self.val = n
        self.children = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = Node("")

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = Node(c)
            curr = curr.children[c]
        curr.end = True

    def search(self, word: str) -> bool:
        queue = deque([self.root])
        for c in word:
            found = False
            for node in range(len(queue)):
                currNode = queue.popleft()
                for child in currNode.children:
                    if c == '.':
                        found = True
                        queue.append(currNode.children[child])
                    else:
                        if c == child:
                            found = True
                            queue.append(currNode.children[child])
            if not found:
                return False
        for n in queue:
            if n.end == True:
                return True
        return False
        
                    