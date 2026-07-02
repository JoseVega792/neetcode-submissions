class DSU:
    def __init__(self, n):
        self.comps = n
        self.parent = [i for i in range(n + 1)]
        self.rank = [1] * (n + 1)
    
    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    
    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)

        if pu == pv:
            return False
        self.comps -= 1
        if self.rank[pu] < self.rank[pv]:
            pu, pv = pv, pu
        self.parent[pu] = self.parent[pv]
        self.rank[pv] += self.rank[pu]
        return True
    
    def components(self):
        return self.comps


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)

        for u,v in edges:
            dsu.union(u,v)
        return dsu.components()