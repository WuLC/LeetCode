import heapq

class Solution:
    def resultsArray(self, queries: List[List[int]], k: int) -> List[int]:
        result, candidates = [], []
        for q in queries:
            distance = abs(q[0]) + abs (q[1])
            if len(candidates) < k:
                heapq.heappush(candidates, -1 * distance)
            else:
                heapq.heappushpop(candidates, -1 * distance)
            result.append(-1 if len(candidates) < k else -1 * candidates[0])
        return result
