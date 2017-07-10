# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2017-07-10 17:18:18
# @Last Modified by:   WuLC
# @Last Modified time: 2017-07-10 17:24:28


# recursive
# referer: https://discuss.leetcode.com/topic/95200/simple-java-recursive-solution
class Solution(object):
    def shoppingOffers(self, price, special, needs):
        """
        :type price: List[int]
        :type special: List[List[int]]
        :type needs: List[int]
        :rtype: int
        """
        result = (1<<31) - 1
        for offer in special:
            validOffer = True
            for i in xrange(len(needs)):
                needs[i] -= offer[i]
                if needs[i] < 0:
                    validOffer = False
            
            if validOffer: # supply can not exceed need
                result = min(result, offer[-1] + self.shoppingOffers(price, special, needs))
            
            # restore
            for i in xrange(len(needs)):
                needs[i] += offer[i]
            
        noOfferSum = sum([price[i] * needs[i] for i in xrange(len(needs))])
        return min(noOfferSum, result)
            
                    
                
            
