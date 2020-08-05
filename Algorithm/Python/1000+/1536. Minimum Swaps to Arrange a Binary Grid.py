from collections import Counter

class Solution(object):
    def minSwaps(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def getZeroCnt(arr):
            cnt, idx = 0, len(arr) - 1
            while idx >=0 and arr[idx] == 0:
                cnt += 1
                idx -= 1
            return cnt
        
        n = len(grid)
        zeroCnts = [getZeroCnt(grid[i]) for i in xrange(n)]
        result = 0
        for i in xrange(n):
            j = i
            while j < n and zeroCnts[j] < n-i-1:
                j += 1
            if j == n:
                return -1
            else:
                result += j - i
                while j > i:
                    zeroCnts[j], zeroCnts[j-1] = zeroCnts[j-1], zeroCnts[j]
                    j -= 1
        return result