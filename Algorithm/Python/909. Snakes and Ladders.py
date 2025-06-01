from collections import deque

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        def getCoordinate(num):
            r, c = num//n, num%n
            if c == 0:
                r -= 1  
            if (r&1) == 0:
                return (n-r-1, (n+c-1)%n)
            else:
                return (n-r-1, (n-c)%n)

        curr, result, dest = 1, 0, n**2
        q, visited = deque([1]), [False]*(dest+1)
        while len(q) > 0:
            cnt = len(q)
            for _ in range(cnt):
                curr = q.popleft()
                if curr >= dest:
                    return result
                for i in range(1,7):
                    _next = min(curr + i, dest)
                    r, c = getCoordinate(_next)
                    if board[r][c] != -1:
                        _next = board[r][c]
                    if not visited[_next]:
                        q.append(_next)
                        visited[_next] = True
            result += 1
        return -1
