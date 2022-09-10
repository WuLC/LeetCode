#
# @lc app=leetcode id=474 lang=python
#
# [474] Ones and Zeroes
#

# @lc code=start

# iterate from backward to forward to avoid copy
class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0]*(n+1) for _ in range(m+1)]
        for s in strs:
            zeros, ones = 0, 0
            for c in s:
                if c == '0':
                    zeros += 1
                else:
                    ones += 1


            for i in range(m, zeros - 1, -1):
                for j in range(n, ones - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i-zeros][j-ones] + 1)
        
        return dp[m][n]


# copy dp matrix
# class Solution(object):
#     def findMaxForm(self, strs, m, n):
#         """
#         :type strs: List[str]
#         :type m: int
#         :type n: int
#         :rtype: int
#         """
#         dp = [[0]*(n+1) for _ in range(m+1)]
#         for s in strs:
#             zeros, ones = 0, 0
#             for c in s:
#                 if c == '0':
#                     zeros += 1
#                 else:
#                     ones += 1
#             if zeros > m or ones > n:
#                 continue
            
#             ori_dp = [row[:] for row in dp]
#             for i in range(m+1):
#                 for j in range(n+1):
#                     if i - zeros >= 0 and j - ones >= 0:
#                         dp[i][j] = max(ori_dp[i][j], ori_dp[i-zeros][j-ones] + 1)
#         return dp[m][n]
        
# @lc code=end

