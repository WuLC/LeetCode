# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2017-04-09 13:36:43
# @Last modified by:   WuLC
# @Last Modified time: 2017-04-09 13:36:58
# @Email: liangchaowu5@gmail.com


# dynamic programming
class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        dp = [0]*(amount+1)
        dp[0] = 1
        coins.sort()
        for coin in coins:
            for i in xrange(coin, amount+1):
                if i < coin:
                    break
                dp[i] += dp[i-coin]
        return dp[amount]
        