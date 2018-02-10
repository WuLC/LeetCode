# -*- coding: utf-8 -*-
# Created on Fri Feb 09 2018 0:18:5
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# bfs 
# it can find the minimum turns by its process naturally
from collections import deque
class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        marker, count = '#', 0
        deadends = set(deadends)
        queue = deque(['0000', marker])
        visited = set()
        while len(queue) > 0:
            q = queue.popleft()
            if q == target:
                return count
            elif q in visited or q in deadends:
                continue
            elif q == marker:
                if len(queue) == 0:
                    return -1
                else:
                    count += 1
                    queue.append(marker)
            else:
                visited.add(q)
                queue.extend(self.nextState(q))
        
    def nextState(self, curr):
        next_state = []
        for i in xrange(len(curr)):
            next_state.append(curr[:i] + str((int(curr[i])-1)%10) + curr[i+1:])
            next_state.append(curr[:i] + str((int(curr[i])+1)%10) + curr[i+1:])
        return next_state