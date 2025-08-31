class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        even_cnt, odd_cnt = m>>1, (m>>1)+(m&1)
        return (n>>1)*odd_cnt + ((n>>1)+(n&1))*even_cnt 