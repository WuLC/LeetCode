#
# @lc app=leetcode id=738 lang=python
#
# [738] Monotone Increasing Digits
#

# @lc code=start
from string import digits
from unicodedata import digit
from unittest import result


class Solution(object):
    def monotoneIncreasingDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        digits, sn = [], str(n)
        for i in range(len(sn)):
            if i+1 < len(sn) and sn[i] > sn[i+1]:
                left = ord(sn[i]) - ord('1')
                digits.append(str(left))
                digits += '9' * (len(sn) -i - 1)
                break
            else:
                digits.append(sn[i])
        
        for i in range(len(digits) - 1, 0, -1):
            if ord(digits[i]) < ord(digits[i-1]):
                digits[i-1] = digits[i]
                digits[i] = '9'
        return int(''.join(digits))

# @lc code=end