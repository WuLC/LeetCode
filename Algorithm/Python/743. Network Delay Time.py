# -*- coding: utf-8 -*-
# Created on Fri Dec 15 2017 23:7:59
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# dijikstra algorithm
class Solution(object):
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        result = [-1] * (N+1)
        visited = [False] * (N+1)
        dist = [[-1] * (N+1) for _ in range(N+1)]
        for (s, e, t) in times:
            dist[s][e] = t
            
        result[K] = 0
        for _ in range(N):
            idx = None
            for i in range(1, N+1):
                if not visited[i] and result[i] != -1 and (idx == None or result[i] < result[idx]):
                    idx = i
            if idx == None:
                return -1
            else:
                visited[idx] = True
                
            for j in range(1, N+1):
                if not visited[j] and dist[idx][j] != -1 and (result[j] == -1 or result[j] > result[idx] + dist[idx][j]):
                    result[j] = result[idx] + dist[idx][j]
        return max(result)
                
        
        