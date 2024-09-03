class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        c1, r1 = coordinate1[0], coordinate1[1]
        c2, r2 = coordinate2[0], coordinate2[1]
        if (ord(c1) - ord('a'))%2 == (ord(c2) - ord('a'))%2:
            return int(r1)%2 == int(r2)%2
        else:
            return int(r1)%2 != int(r2)%2
