# brute-force with backtracking

class Solution(object):
    def maximumRequests(self, n, requests):
        """
        :type n: int
        :type requests: List[List[int]]
        :rtype: int
        """
        self.result = 0
        record = [0] * n
        self.dfs(0, requests, record, 0)
        return self.result

    def dfs(self, idx, requests, record, cnt):
        if all(num == 0 for num in record):
            self.result = max(self.result, cnt)
        for i in range(idx, len(requests)):
            record[requests[i][0]] -= 1
            record[requests[i][1]] += 1
            self.dfs(i+1, requests, record, cnt+1)
            record[requests[i][0]] += 1
            record[requests[i][1]] -= 1