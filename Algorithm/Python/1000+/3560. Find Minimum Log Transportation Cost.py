class Solution:
    def minCuttingCost(self, n: int, m: int, k: int) -> int:
        result = 0
        for log in (m, n):
            if log > k:
                result += k*(log-k)
        return result
        