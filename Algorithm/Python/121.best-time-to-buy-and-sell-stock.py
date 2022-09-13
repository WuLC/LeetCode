#
# @lc app=leetcode id=121 lang=python
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        result, curr_min = 0, 100000 # since all prices[i] <= 10^4
        for p in prices:
            result = max(result, p - curr_min)
            curr_min = min(curr_min, p)
        return result
        
# @lc code=end

