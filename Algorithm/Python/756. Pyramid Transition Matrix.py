# -*- coding: utf-8 -*-
# Created on Wed Jan 31 2018 13:28:17
# Author: WuLC
# EMail: liangchaowu5@gmail.com


# use generator for dfs
from collections import defaultdict
class Solution(object):
    def pyramidTransition(self, bottom, allowed):
        """
        :type bottom: str
        :type allowed: List[str]
        :rtype: bool
        """
        self.build = defaultdict(list)
        for tri in allowed:
            bot, up = tri[:2], tri[2]
            self.build[bot].append(up)
        return self.dfs(bottom)
    
    def dfs(self, curr_bottom):
        if len(curr_bottom) == 1:
            return True
        return any(self.dfs(next_bottom) for next_bottom in self.generate_upper(curr_bottom, [], 0))
    
    def generate_upper(self, curr_bottom, next_bottom, idx):
        if idx == len(curr_bottom) - 1:
            yield ''.join(next_bottom)
        bot = curr_bottom[idx:idx+2]
        for up in self.build[bot]:
            next_bottom.append(up)
            for result in self.generate_upper(curr_bottom, next_bottom, idx+1):
                yield result
            next_bottom.pop()
        
        