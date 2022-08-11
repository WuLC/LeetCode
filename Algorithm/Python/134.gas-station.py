#
# @lc app=leetcode id=134 lang=python
#
# [134] Gas Station
#

# @lc code=start
class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        n = len(gas)
        diff = [gas[i] - cost[i] for i in range(n)]

        idx, curr_sum, count = 0, 0, 0
        result = -1
        while idx < n:
            new_idx = idx
            for i in range(n):
                ni = (idx+i) % n
                curr_sum += diff[ni]
                if curr_sum < 0:
                    curr_sum, count = 0, 0
                    new_idx = ni
                    break
                count += 1
            if count == n:
                result = idx
                break
            idx = max(idx+1, new_idx+1)
        return result
            
        
# @lc code=end

