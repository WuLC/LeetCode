# greedy
# distribute resources greedily according to marginal revenue
import heapq
from collections import defaultdict

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        heap, counter = [], defaultdict(int)
        n = len(classes)
        # init heap
        for i in range(n):
            p, n = classes[i]
            heapq.heappush(heap, (-1.0*(p+1)/(n+1), i))
        
        # distribute extra studenst
        while extraStudents > 0:
            _, i = heapq.heappop(heap)
            counter[i] += 1
            p, n = classes[i]
            heapq.heappush(heap, (-1.0*(p+counter[i]+1)/(n+counter[i]+1), i))
            extraStudents -= 1
        
        return sum((classes[i][0]+counter[i])/(classes[i][1]+counter[i]) for i in range(n))/n
        

    
# WA dp
class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        m, n = len(classes), extraStudents
        dp = [[0]*(n+1) for _ in range (m+1)]
        for i in range(1, m+1):
            for j in range(n+1):
                p, t = classes[i-1][0], classes[i-1][1]
                if j == 0:
                    dp[i][j] = ((i-1)*dp[i-1][j] + p/t)/i
                else:
                    dp[i][j] = max((p+1)/(t+1) + (i-1)*dp[i-1][j-1],
                                   (i-1)*dp[i-1][j] + p/t)/i
        return dp[-1][-1]