#coding: utf8

class Solution(object):
    def beautifulArray(self, N):
        """
        :type N: int
        :rtype: List[int]
        """
        result = [1]
        while len(result) < N:
            odds, evens = [], []
            for num in result:
                if num*2 - 1 <= N:
                    odds.append(num*2 - 1)
                if num*2 <= N:
                    evens.append(num*2)
            result = odds + evens
        return result