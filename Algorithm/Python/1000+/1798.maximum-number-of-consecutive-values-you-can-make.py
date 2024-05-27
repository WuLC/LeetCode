#
# @lc app=leetcode id=1798 lang=python
#
# [1798] Maximum Number of Consecutive Values You Can Make
#

# @lc code=start

# solution got TLE with time complexiy O(mn)
# m=len(coins), n=sum(coins)
class Solution1(object):
    def getMaximumConsecutive(self, coins):
        """
        :type coins: List[int]
        :rtype: int
        """
        m, n = len(coins), sum(coins)
        available = [False] * (n+1)
        dp = [[False]*(n+1) for _ in range(m+1)]
        available[0], dp[0][0] = True, True
        for i in range(m):
            for j in range(n+1):
                if j == 0:
                    dp[i+1][j] = True
                elif j-coins[i] >= 0:
                    dp[i+1][j] |= dp[i][j-coins[i]] # take the current coin
                dp[i+1][j] |= dp[i][j] # do not take the current coint
                available[j] |= dp[i+1][j]

        count = 0
        for i in range(n+1):
            if available[i] == True:
                count += 1
            else:
                break
        return count

# sort with simple rule, time complexity O(nlogn)
# three rules
# (1) if you can make the first x values and you have a value v, then you can make all the values ≤ v + x
# (2) sort the array to start with 0
class Solution(object):
    def getMaximumConsecutive(self, coins):
        """
        :type coins: List[int]
        :rtype: int
        """
        coins.sort()
        curr_sum = 0
        for i in range(len(coins)):
            if curr_sum + 1 < coins[i]:
                break
            curr_sum += coins[i]
        return curr_sum+1

# @lc code=end

