class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        result = numBottles
        while numBottles >= numExchange:
            fullExchange, numBottles = divmod(numBottles, numExchange)
            numBottles += fullExchange
            result += fullExchange
        return result