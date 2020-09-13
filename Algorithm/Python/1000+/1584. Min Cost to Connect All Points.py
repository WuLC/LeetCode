class UnionFindSet(object):
    def __init__(self, n):
        self.parents =[i for i in range(n)]
        self.height = [0] * n
    
    def find(self, v):
        if self.parents[v] != v:
            self.parents[v] = self.find(self.parents[v])
        return self.parents[v]
    
    def union(self, p1, p2):
        assert p1 != p2, "same parent need no union"
        if self.height[p1] == self.height[p2]:
            self.parents[p2] = p1
            self.height[p1] += 1
        elif self.height[p1] > self.height[p2]:
            self.parents[p2] = p1
        else:
            self.parents[p1] = p2


class Solution(object):
    def minCostConnectPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        def manhateen_dist(i, j):
            return abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
        n = len(points)
        distances =sorted([(i, j, manhateen_dist(i, j)) 
                            for i in range(n) for j in range(i+1, n)],
                         key=lambda x: x[2])
        result = 0
        ufs = UnionFindSet(n)
        for n1, n2, d in distances:
            p1, p2 = ufs.find(n1), ufs.find(n2)
            if p1 != p2:
                result += d
                ufs.union(p1, p2)
        return result