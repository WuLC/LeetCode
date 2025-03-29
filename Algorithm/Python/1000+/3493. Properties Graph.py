class Solution:
    def numberOfComponents(self, properties: List[List[int]], k: int) -> int:
        n = len(properties)
        ufs = UnionFindSet(n)
        for i in range(n):
            for j in range(i+1, n):
                if self.intersect(properties[i], properties[j], k):
                    ufs.union(i, j)
        return ufs.connected_cnt()
                

    def intersect(self, p1: List[int], p2: List[int], k: int) -> bool:
        s1, s2 = set(p1), set(p2)
        return sum(1 if num in s2 else 0 for num in s1) >= k


class UnionFindSet:
    def __init__(self, n):
        self.parents = [i for i in range(n)]

    def find(self, i):
        if self.parents[i] != i:
            self.parents[i] = self.find(self.parents[i])
        return self.parents[i]

    def union(self, i, j):
        pi, pj = self.find(i), self.find(j)
        if pi < pj:
            self.parents[pj] = pi
        else:
            self.parents[pi] = pj

    def connected_cnt(self):
        result = set()
        for i in range(len(self.parents)):
            result.add(self.find(i))
        return len(result)
            