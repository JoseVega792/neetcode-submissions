class DSU:
    def __init__(self, n):
        self.comp = n
        self.parent = [i for i in range(n + 1)]
        self.rank = [1] * (n + 1) 

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)

        if px == py:
            return False
        
        self.comp -= 1
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.rank[px] += self.rank[py]
        self.parent[py] = px
        return True

    def components(self):
        return self.comp

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n - 1:
            return False
        
        dsu = DSU(n)
        for u, v in edges:
            if not dsu.union(u,v):
                return False
        return dsu.components() == 1