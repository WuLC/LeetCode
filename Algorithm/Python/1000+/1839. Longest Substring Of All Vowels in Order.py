class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        n, result = len(word), 0
        idx, left = 0, 0
        candidate = set()
        while idx < n:
            if word[idx] == 'a' and len(candidate) == 0:
                left = idx
                candidate.add(word[idx])
            valid = all(ord(word[idx]) >= ord(c) for c in candidate)
            if valid:
                candidate.add(word[idx])
                if word[idx] == 'u' and len(candidate) == 5:
                    result = max(result, idx-left+1)
                    print(idx, left)
            else:
                candidate.clear()
                continue
            idx += 1  
        return result