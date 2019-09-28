from collections import defaultdict
class UnionFindSet():
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.depth = [1] * n
        
    def find_parent(self, v):
        if self.parent[v] != v:
            self.parent[v] = self.find_parent(self.parent[v])
        return self.parent[v]
        
    def union(self, v1, v2):
        p1, p2 = self.find_parent(v1), self.find_parent(v2)
        if p1 == p2:
            return
        if self.depth[p1] < self.depth[p2]:
            self.parent[p1] = p2
        elif self.depth[p1] > self.depth[p2]:
            self.parent[p2] = p1
        else:
            self.parent[p2] = p1
            self.depth[p1] += 1
        
        
class Solution(object):
    def smallestStringWithSwaps(self, s, pairs):
        """
        :type s: str
        :type pairs: List[List[int]]
        :rtype: str
        """
        n = len(s)
        ufs = UnionFindSet(n)
        for p in pairs:
            ufs.union(p[0], p[1])
        idxs, chars = defaultdict(list), defaultdict(list)
        for i, c in enumerate(s):
            p = ufs.find_parent(i)
            idxs[p].append(i)
            chars[p].append(c)
        result = [c for c in s]
        for k, v in idxs.items():
            print(sorted(idxs[k]), sorted(chars[k]))
            for i, c in zip(sorted(idxs[k]), sorted(chars[k])):
                result[i] = c
        return ''.join(result)
        