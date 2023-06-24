#
# @lc app=leetcode id=950 lang=python
#
# [950] Reveal Cards In Increasing Order
#

# @lc code=start
class Solution(object):
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        if len(deck) <= 2:
            return sorted(deck)
        
        deck.sort()
        mid = len(deck)>>1
        right = self.deckRevealedIncreasing(deck[mid:][:])
        if len(right) > mid:
            right.append(right[0])
            right.pop(0)

        # reorganize
        result = []
        i, j = 0, 0
        while i < mid or j < len(right):
            if i < mid:
                result.append(deck[i])
                i += 1
            if j < len(right):
                result.append(right[j])
                j += 1
        return result
        
if __name__ == "__main__":
    data = [17,13,11,2,3,5,7]
    s = Solution()
    print(s.deckRevealedIncreasing(data))
# @lc code=end

