# prefix sum and bit manipulation, time complexity: O(n)
from collections import defaultdict

class Solution(object):
    def wonderfulSubstrings(self, word):
        """
        :type word: str
        :rtype: int
        """
        n, result = len(word), 0
        counter, prefix = defaultdict(int), 0
        counter[0] = 1
        for i in range(n):
            prefix ^= (1 << (ord(word[i]) - ord('a')))
            result += counter[prefix]
            counter[prefix] += 1
            for j in range(10):
                tmp = prefix^(1<<j)
                if tmp in counter:
                    result += counter[tmp]
        return result

#################################################
# naive solution, time complexity:O(n^2), TLE
from collections import defaultdict

class Solution(object):
    def wonderfulSubstrings(self, word):
        """
        :type word: str
        :rtype: int
        """
        n, result = len(word), 0
        for i in range(n):
            counter, odd_cnt = defaultdict(int), 0
            for j in range(i, n):
                counter[word[j]] += 1
                if (counter[word[j]] & 1) == 1:
                    odd_cnt += 1
                elif counter[word[j]] > 1:
                    odd_cnt -= 1
                if odd_cnt <= 1:
                    result += 1
        return result
                


