class Solution:
    def clearStars(self, s: str) -> str:
        idx = [[] for _ in range(26)]
        chars = [c for c in s]
        base = ord('a')
        for i in range(len(s)):
            if s[i] == '*':
                for j in range(26):
                    if len(idx[j]) > 0:
                        chars[idx[j].pop()] = '*'
                        break
            else:
                idx[ord(s[i])-base].append(i)
        return ''.join(c for c in chars if c != '*')