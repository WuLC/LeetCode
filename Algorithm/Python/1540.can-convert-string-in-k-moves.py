#
# @lc app=leetcode id=1540 lang=python
#
# [1540] Can Convert String in K Moves
#

# @lc code=start

# use fixed-len counter instead of set to avoid TLE
class Solution(object):
    def canConvertString(self, s, t, k):
        """
        :type s: str
        :type t: str
        :type k: int
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        counter = [0] * 26
        for i in range(len(s)):
            diff = (ord(t[i]) - ord(s[i]) + 26) % 26
            if diff > 0 and diff + counter[diff] * 26 > k:
                return False
            counter[diff] += 1
        return True


# # TLE
# class Solution(object):
#     def canConvertString(self, s, t, k):
#         """
#         :type s: str
#         :type t: str
#         :type k: int
#         :rtype: bool
#         """
#         if len(s) != len(t):
#             return False
#         used = set()
#         for i in range(len(s)):
#             diff = ord(t[i]) - ord(s[i])
#             # print("{}:{}".format(s[i], diff))
#             if diff != 0:
#                 convert = False
#                 while diff <= k:
#                     if diff > 0 and diff not in used:
#                         used.add(diff)
#                         convert = True
#                         break
#                     diff += 26
#                 if not convert:
#                     return False                    
#         return True
     
# @lc code=end

