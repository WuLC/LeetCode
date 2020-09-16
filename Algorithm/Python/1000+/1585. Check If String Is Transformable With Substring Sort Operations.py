
# greedy, O(m+n) time

from collections import defaultdict
class Solution(object):
    def isTransformable(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        idx = defaultdict(list)
        for i in range(len(s)):
            idx[s[i]].append(i)
            
        counter = defaultdict(int)
        for c in t:
            if counter[c] >= len(idx[c]):
                return False
            num = ord(c) - 48
            for i in range(num):
                sc = chr(48+i)
                if counter[sc] < len(idx[sc]) and idx[sc][counter[sc]] < idx[c][counter[c]]:
                    return False
            counter[c] += 1
        return True
        
        
        