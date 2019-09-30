class Solution(object):
    def removeDuplicates(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        chars, count = [], []
        for c in s:
            if len(chars) > 0 and c == chars[-1]:
                count[-1] += 1
            else:
                chars.append(c)
                count.append(1)
            if count[-1] == k:
                count.pop()
                chars.pop()
        return ''.join([c*n for c, n in zip(chars, count)])
        