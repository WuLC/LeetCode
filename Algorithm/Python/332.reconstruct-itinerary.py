#
# @lc app=leetcode id=332 lang=python
#
# [332] Reconstruct Itinerary
#

# @lc code=start
from collections import defaultdict


class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        self.result =  ["JFK"]
        self.paths, self.used = defaultdict(list), defaultdict(list)

        for start, end in tickets:
            self.paths[start].append(end)
            self.used[start].append(False)
        
        for k in self.paths.keys():
            self.paths[k].sort()

        self.dfs("JFK", 0, tickets)
        return self.result
    
    def dfs(self, s, count, tickets):
        if count == len(tickets):
            return
        for i in range(len(self.paths[s])):
            if not self.used[s][i]:
                self.used[s][i] = True
                self.result.append(self.paths[s][i])
                self.dfs(self.paths[s][i], count+1, tickets)
                if self.result:
                    return
                self.result.pop()
                self.used[s][i] = False
          

# @lc code=end

