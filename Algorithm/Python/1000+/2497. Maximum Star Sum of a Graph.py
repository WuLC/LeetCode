from collections import defaultdict
import heapq

class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        neighbors = defaultdict(list)
        for s, e in edges:
            neighbors[s].append(vals[e])
            neighbors[e].append(vals[s])
        
        result = max(vals)
        for center, neighbor in neighbors.items():
            k_neighbors = heapq.nlargest(k, neighbor)
            # 写法一
            # result = max(result, vals[center]+sum(num if num > 0 else 0 for num in k_neighbors))
            # 写法二
            result = max(result, vals[center]+sum(num for num in k_neighbors if num > 0))
        return result

# 可以在构建图的时候就把 < 0 的 neighbor 卡掉，这样时间复杂度会更小
class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        neighbors = defaultdict(list)
        for s, e in edges:
            if vals[e] > 0:
                neighbors[s].append(vals[e])
            if vals[s] > 0:
                neighbors[e].append(vals[s])
        
        result = max(vals)
        for center, neighbor in neighbors.items():
            result = max(result, vals[center]+sum(heapq.nlargest(k, neighbor)))
        return result
