from collections import defaultdict, deque
class Solution(object):
    def minReorder(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        neighbor, direction = defaultdict(set), defaultdict(set)
        queue, visited = deque([0]), set()
        for start, end in connections:
            direction[start].add(end)
            neighbor[start].add(end)
            neighbor[end].add(start)
        
        result = 0
        while len(queue) > 0:
            curr = queue.popleft()
            visited.add(curr)
            for node in neighbor[curr]:
                if node in visited:
                    continue
                if curr not in direction[node]:
                    result += 1
                queue.append(node)
        return result                   