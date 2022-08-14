#
# @lc app=leetcode id=135 lang=python
#
# [135] Candy
#

# @lc code=start
class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        candies = [1] * len(ratings)
        
        # make left->right legal
        for i in range(len(ratings) - 1):
            if ratings[i+1] > ratings[i]:
                candies[i+1] = candies[i] + 1
        
        # make right->left legal
        for i in range(len(ratings)-1, 0, -1):
            if ratings[i-1] > ratings[i]:
                candies[i-1] = max(candies[i-1], candies[i]+1)
        return sum(candies)
        
# @lc code=end

