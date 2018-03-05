# -*- coding: utf-8 -*-
# Created on Fri Feb 23 2018 23:42:38
# Author: WuLC
# EMail: liangchaowu5@gmail.com


# bfs, TLE
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

        count, marker = 0, -1        
        queue = deque([src, marker])
        prices = {src:0}
        while count <= K and len(queue) > 0:
            city = queue.popleft()
            if city == marker:
                count += 1
                queue.append(marker)
            else:
                for k, v in route[city].items():
                    prices[k] = prices[city] + v if k not in prices else min(prices[k], prices[city] + v)
                    queue.append(k)
        return prices[dst] if dst in prices else -1