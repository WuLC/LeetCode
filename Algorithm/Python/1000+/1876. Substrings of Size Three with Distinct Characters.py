from collections import defaultdict

class Solution(object):
    def countGoodSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        counter = defaultdict(int)
        for i in range(len(s)):
            counter[s[i]] += 1
            if i > 2:
                c = s[i-3]
                counter[c] -= 1
                if counter[c] == 0:
                    counter.pop(c)
            if len(counter) == 3:
                result += 1
        return result
