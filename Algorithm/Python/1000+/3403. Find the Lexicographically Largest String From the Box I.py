
# greedy with rule
from collections import defaultdict
class Solution(object):
    def answerString(self, word, numFriends):
        """
        :type word: str
        :type numFriends: int
        :rtype: str
        """
        if numFriends == 1:
            return word
            
        indices, lc = defaultdict(list), 'a'
        for i in range(len(word)):
            indices[word[i]].append(i)
            if ord(word[i]) > ord(lc):
                lc = word[i]

        n, result = len(word), ""
        for idx in indices[lc]:
            candidate = ""
            if idx >= numFriends - 1:
                candidate = word[idx:]
            else:
                candidate = word[idx: n - (numFriends-idx-1)]
            result = self.getLargestString(result, candidate)
        return result

    def getLargestString(self, w1, w2):
        for i in range(min(len(w1), len(w2))):
            if ord(w1[i]) > ord(w2[i]):
                return w1
            elif ord(w1[i]) < ord(w2[i]):
                return w2
        return w1 if len(w1) > len(w2) else w2
    


# naive dfs results TLE
class Solution(object):
    def answerString(self, word, numFriends):
        """
        :type word: str
        :type numFriends: int
        :rtype: str
        """
        result = [""]
        self.dfs(word, numFriends, result)
        return result[0]

    def dfs(self, word, numFriends, result):
        largest = ""
        if numFriends == 1:
            largest = word
        else:
            for i in range(len(word) - numFriends + 1):
                w1 = word[:i+1]
                w2 = self.dfs(word[i+1:], numFriends-1, result)
                largest = self.getLargestString(self.getLargestString(w1, w2), largest)
        result[0] = self.getLargestString(result[0], largest)
        return largest

    def getLargestString(self, w1, w2):
        for i in range(min(len(w1), len(w2))):
            if ord(w1[i]) > ord(w2[i]):
                return w1
            elif ord(w1[i]) < ord(w2[i]):
                return w2
        return w1 if len(w1) > len(w2) else w2
    
