from collections import defaultdict

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        record, count = defaultdict(int), 0
        for w in words:
            rw = w[1]+w[0]
            if record[rw] > 0:
                record[rw] -= 1
                count += 2
            else:
                record[w] += 1
        
        for w, cnt in record.items():
            if cnt > 0 and w[0] == w[1]:
                count +=1 
                break
        return count<<1

