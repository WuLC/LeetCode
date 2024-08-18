from collections import defaultdict
class Solution(object):
    def countKConstraintSubstrings(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        left, right, result = 0, 0, 0
        counter = defaultdict(int)
        while left <= right and right < len(s):
            counter[s[right]] += 1
            while counter['0'] > k and counter['1'] > k:
                counter[s[left]] -= 1
                left += 1
            result += right - left + 1
            right += 1
        return result
            