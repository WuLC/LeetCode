# AC solution
# try dynamic programming when facing subsequence problem
class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        n = len(words)
        length, indices = [1] * n, [[] for _ in range(n)]
        result = [0, 0]

        for i in range(n):
            for j in range(i):
                if groups[i] != groups[j] and self.isLegalWords(words[i], words[j]):
                    if length[j] + 1 > length[i]:
                        indices[i] = indices[j][:]
                        length[i] = length[j] + 1
            indices[i].append(i)
            if length[i] > result[0]:
                result = length[i], i
        
        return [words[i] for i in indices[result[1]]]

    def isLegalWords(self, w1, w2):
        if len(w1) != len(w2):
            return False
        cnt = 0
        for i in range(len(w1)):
            if w1[i] != w2[i]:
                cnt += 1
            if cnt > 1:
                return False
        return True if cnt == 1 else False


# TLE solution
# brute force with backtracking will lead to TLE
class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        def dfs(idx, cand):
            nonlocal indices # py3
            if len(cand) > len(indices):
                indices = cand[:]
            for i in range(idx, n):
                if len(cand) == 0 or (groups[i] != groups[cand[-1]] 
                        and self.isLegalWords(words[i], words[cand[-1]])):
                    cand.append(i)
                    dfs(i+1, cand)
                    cand.pop()

        n, indices = len(words), []
        dfs(0, [])
        return [words[i] for i in indices]
            
    def isLegalWords(self, w1, w2):
        if len(w1) != len(w2):
            return False
        cnt = 0
        for i in range(len(w1)):
            if w1[i] != w2[i]:
                cnt += 1
            if cnt > 1:
                return False
        return True if cnt == 1 else False
                    