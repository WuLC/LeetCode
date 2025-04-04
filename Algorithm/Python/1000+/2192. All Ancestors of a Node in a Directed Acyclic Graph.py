# dfs with ascending order source to make result in order
# use visited set to reduce time complexity
from collections import defaultdict

class Solution(object):
    def getAncestors(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[List[int]]
        """
        graph = defaultdict(list)
        for s, e in edges:
            graph[s].append(e)
        
        result = [[] for _ in range(n)]

        for i in range(n):
            self.dfs(i, i, graph, result, set())
        return result

    def dfs(self, parent, curr, graph, result, visited):
        if parent != curr:
            result[curr].append(parent)

        if curr not in graph:
            return
        for neigh in graph[curr]:
            if neigh in visited:
                continue
            visited.add(neigh)
            self.dfs(parent, neigh, graph, result, visited)

"""
# naive dfs, TLE
from collections import defaultdict
class Solution(object):
    def getAncestors(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[List[int]]
        """
        self.index = defaultdict(list)
        for s, e in edges:
            self.index[s].append(e)
        
        self.result = [set() for _ in range(n)]

        for start, _ in self.index.items():
            self.dfs(start, [start])
        
        return [sorted(list(ans)) for ans in self.result]
        

    def dfs(self, curr, path):
        if curr not in self.index:
            tmp = set()
            tmp.add(path[0])
            for j in range(1, len(path)):
                self.result[path[j]] = self.result[path[j]].union(tmp)
            return
        for i in range(len(self.index[curr])):
            path.append(self.index[curr][i])
            self.dfs(self.index[curr][i], path)
            path.pop()
"""
        
