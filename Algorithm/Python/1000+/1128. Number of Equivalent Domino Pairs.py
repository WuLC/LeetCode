from collections import defaultdict
class Solution(object):
    def numEquivDominoPairs(self, dominoes):
        """
        :type dominoes: List[List[int]]
        :rtype: int
        """
        counter = defaultdict(int)
        result = 0
        for a, b in dominoes:
            flag = (a, b) if a <= b else (b, a)
            result += counter[flag]
            counter[flag] += 1
        return result