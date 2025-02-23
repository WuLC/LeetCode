class Solution(object):
    def hasSameDigits(self, s):
        """
        :type s: str
        :rtype: bool
        """
        digits = [int(c) for c in s]
        while len(digits) > 2:
            digits = [(digits[i]+digits[i+1])%10 for i in range(len(digits)-1)]
        return digits[0] == digits[1]