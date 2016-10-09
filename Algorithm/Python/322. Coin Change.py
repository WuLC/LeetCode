# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-08-23 08:49:28
# @Last modified by:   WuLC
# @Last Modified time: 2016-08-23 14:46:30
# @Email: liangchaowu5@gmail.com


# same method written in Java get AC, but TLE for Python

# DP, from bottom to top, TLE
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [None for i in xrange(amount+1)]
        dp[0] = 0
        for i in xrange(1, amount+1):
            tmp = None
            for coin in coins:
                if i>=coin and dp[i-coin]!=None:
                    tmp = dp[i-coin]+1 if tmp == None else min(tmp, dp[i-coin]+1)
            dp[i] = tmp
        return dp[amount] if dp[amount]!=None else -1


# DP, from top to bottom, TLE
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        cache = {}
        cache[0] = 0
        return self.helper(coins, amount, cache)
        
    
    def helper(self, coins, amount, cache):
        if amount in cache:
            return cache[amount]
        min_coins = amount + 1
        for coin in coins:
            if amount >= coin:
                count = 1
                left = self.helper(coins, amount - coin, cache)
                if left != -1:
                    count += left 
                    min_coins = min(min_coins, count)
        cache[amount] = min_coins if min_coins != amount+1 else -1
        return cache[amount]

# backtracking, TLE
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        result = []
        coins.sort()
        self.helper(0, coins, amount, 0, result)
        return result[0] if result else -1
        
    def helper(self, idx, coins, amount, count, result):
        if amount == 0:
            if result:
                result[0] = min(result[0], count)
            else:
                result.append(count)
            return
        for i in xrange(idx, len(coins)):
            if amount >= coins[i]:
                self.helper(i, coins, amount-coins[i], count+1, result)
            else:
                return