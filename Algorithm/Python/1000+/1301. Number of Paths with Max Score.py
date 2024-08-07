# naive dfs, TLE
from collections import defaultdict

class Solution(object):
    def pathsWithMaxScore(self, board):
        """
        :type board: List[str]
        :rtype: List[int]
        """
        m, n = len(board), len(board[0])
        candidates = defaultdict(int)
        result = [0, 0]
        def dfs(i, j, _sum): 
            if board[i][j] == 'E':
                candidates[_sum] += 1
                return
            curr_num = int(board[i][j]) if board[i][j].isdigit() else 0
            for d in ((1, 0), (0, 1), (1, 1)):
                ni, nj = i-d[0], j-d[1]
                if ni >= 0 and nj >= 0 and board[ni][nj] != 'X':
                    dfs(ni, nj, _sum+curr_num)
        
        dfs(m-1, n-1, 0)
        for k, v in candidates.items():
            if result[0] <= k:
                result[0], result[1] = k, v
        return result

# dfs with cache to avoid TLE
from collections import defaultdict

class Solution(object):
    def pathsWithMaxScore(self, board):
        """
        :type board: List[str]
        :rtype: List[int]
        """
        m, n = len(board), len(board[0])
        memo = defaultdict(list)

        def dfs(i, j): 
            """
            return: [can reach E from (i, j), max_sum, number of such paths]
            """
            if board[i][j] == 'E':
                return [1, 0, 1]
            elif board[i][j] == 'X':
                return [0, 0, 0]

            flag = (i, j)
            if flag not in memo:
                counter = defaultdict(int)
                for d in ((1, 0), (0, 1), (1, 1)):
                    ni, nj = i-d[0], j-d[1]
                    if ni >= 0 and nj >= 0:
                        if (ni, nj) not in memo:
                            memo[(ni, nj)] = dfs(ni, nj)
                        _reach, _sum, _cnt = memo[(ni, nj)]
                        if _reach:
                            counter[_sum] += _cnt
                
                curr_num = int(board[i][j]) if board[i][j].isdigit() else 0
                memo[flag] = [0, 0, 0]
                for k, v in counter.items():
                    if k+curr_num >= memo[flag][1]:
                        memo[flag][0], memo[flag][1], memo[flag][2] = 1, k+curr_num, v
            return memo[flag]

        _reach, _sum, _cnt = dfs(m-1, n-1)
        modulo = 10**9 + 7
        return [_sum%modulo, _cnt%modulo] if _reach else [0, 0]