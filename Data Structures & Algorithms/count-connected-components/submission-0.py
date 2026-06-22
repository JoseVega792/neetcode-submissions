class DSU:
    def __init__(self,n):
        self.comps = n
        self.Parent = list(range(n))
        self.Size = [1] * (n + 1) 

    def find(self, node):
        if self.Parent[node] != node:
            self.Parent[node] = self.find(self.Parent[node])
        return self.Parent[node]
    
    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)
        if pu != pv:
            self.comps -= 1
            if self.Size[pv] < self.Size[pu]:
                pu, pv = pv, pu
            self.Size[pv] += self.Size[pu]
            self.Parent[pu] = pv 

    def components(self):
        return self.comps

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)
        for x,y in edges:
            dsu.union(x,y)
        return dsu.components()