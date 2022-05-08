#
# @lc app=leetcode id=76 lang=python
#
# [76] Minimum Window Substring
#

# @lc code=start

from collections import Counter

# class Solution(object):
#     def minWindow(self, s, t):
#         """
#         :type s: str
#         :type t: str
#         :rtype: str
#         """
#         if len(s) < len(t):
#             return ""
#         current_counter, target_counter = Counter(), Counter(t)
#         result = [0, 0]
#         left, right = 0, 0
#         while right <= len(s):
#             while all(current_counter[k] >= v for k, v in target_counter.items()):
#                 if result[0] == result[1] or right - left < result[1] - result[0]:
#                     result[0], result[1] = left, right
#                 current_counter[s[left]] -= 1
#                 left += 1
#             if right < len(s):
#                 current_counter[s[right]] += 1
#             right += 1
#         return s[result[0]:result[1]]
        
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        counter = Counter()
        for c in t:
            counter[c] += 1
        min_start, min_len = -1, 0
        left, right, valid_c = 0, 0, len(t)
        while right <= len(s):
            while valid_c == 0:
                if min_start < 0 or min_len > right - left:
                    min_start = left
                    min_len = right - left
                counter[s[left]] += 1
                if counter[s[left]] > 0:
                    valid_c += 1
                left += 1
            
            if right < len(s):
                if counter[s[right]] > 0:
                    valid_c -= 1    
                counter[s[right]] -= 1
            right += 1
        return s[min_start: min_start+min_len]

# @lc code=end

