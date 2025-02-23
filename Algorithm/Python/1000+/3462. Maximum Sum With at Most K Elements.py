import heapq

class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        # AC version
        candidates = []
        for row, limit in zip(grid, limits):
            candidates += heapq.nlargest(min(k, limit), row)
        return sum(heapq.nlargest(k, candidates))

        # TLE
        # merged_heap = []
        # for i in range(len(grid)):
        #     limit_sorted_list = sorted(grid[i], reverse=True)[:min(k, limits[i])]
        #     merged_heap = heapq.merge(merged_heap, limit_sorted_list, reverse=True)
        # return sum(itertools.islice(merged_heap, k))