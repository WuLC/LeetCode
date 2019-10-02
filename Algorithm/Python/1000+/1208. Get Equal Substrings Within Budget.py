class Solution(object):
    def equalSubstring(self, s, t, maxCost):
        """
        :type s: str
        :type t: str
        :type maxCost: int
        :rtype: int
        """
        diff = [abs(ord(a) - ord(b)) for a, b in zip(s, t)]
        result, curr, p1, p2 = 0, 0, 0, 0
        while p2 < len(diff):
            curr += diff[p2]
            if curr <= maxCost:
                result = max(result, p2 - p1 + 1)
            while curr > maxCost:
                curr -= diff[p1]
                p1 += 1
            p2 += 1
        return result
