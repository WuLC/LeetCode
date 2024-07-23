class Solution(object):
    def removeAlmostEqualCharacters(self, word):
        """
        :type word: str
        :rtype: int
        """
        n = len(word)
        remove, remain = [0] * n, [0] * n 
        # each idx has two status: remain or remove
        # two dp array represents two array of whether to remove or remain the current char
        for i in range(n):
            if i == 0:
                remove[i], remain[i] = 1, 0
            else:
                if abs(ord(word[i]) - ord(word[i-1])) <= 1:
                    remain[i] = remove[i-1]
                else:
                    remain[i] = min(remain[i-1], remove[i-1])
                remove[i] = min(remain[i-1], remove[i-1]) + 1 
        return min(remove[-1], remain[-1])
        