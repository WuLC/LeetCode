from collections import Counter

class Solution(object):
    def smallestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        sorted_counter = sorted(Counter(s).items())

        left, right, mid = '', '', ''
        for k, v in sorted_counter:
            if (v&1) == 1:
                mid = k
            tmp = k*(v>>1)
            left += tmp
            right = tmp + right
        return left + mid + right