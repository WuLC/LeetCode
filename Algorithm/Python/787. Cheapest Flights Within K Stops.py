# -*- coding: utf-8 -*-
# Created on Fri Feb 23 2018 23:42:38
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# dp
from collections import deque, defaultdict
class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        route = defaultdict(dict)
        for f in flights:
            s, d, p = f
            route[s][d] = p
        
        count, result = 0, -1
        curr = {src:0}
        while count <= K:
            next = {}
            for s, p in curr.items():
                for k, v in route[s].items():
                    next[k] = p + v if k not in next else min(next[k], p+v)
            if dst in next:
                result = next[dst] if result == -1 else min(result, next[dst])
            curr = next
            count += 1
        return result
                    
    