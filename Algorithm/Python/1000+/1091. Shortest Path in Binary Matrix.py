from collections import deque
class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[1])
        if grid[0][0] != 0 or grid[m-1][n-1] != 0:
            return -1
        queue = deque([(0, 0, 1)])
        grid[0][0] = -1
        result = -1
        while queue:
            curr = queue.popleft()
            r, c = curr[0], curr[1]
            if r == m - 1 and c == n - 1:
                if result == -1:
                    result = curr[2]
                else:
                    result = min(result, curr[2])
            for i in [-1, 0, 1]:
                for j in [-1, 0, 1]:
                    if 0 <= r + i < m and 0 <= c + j < n and grid[r+i][c+j] == 0:
                        queue.append((r+i , c+j, curr[2]+1))
                        grid[r+i][c+j] = -1
        return result
