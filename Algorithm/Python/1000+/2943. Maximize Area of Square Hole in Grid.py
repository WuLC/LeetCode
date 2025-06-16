# MLE solution, simulate the process
# O(m+n) space complexity
# O(h*n+v*m), h and v are the size of removable bars
class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        hb, vb = [1]*(n+2), [1]*(m+2)
        h_cand, v_cand = set(), set()
        hBars.sort()
        vBars.sort()
        self.get_candidate_len(h_cand, hb, hBars)
        self.get_candidate_len(v_cand, vb, vBars)

        if n > m:
            h_cand, v_cand = v_cand, h_cand

        for i in range(max(m,n)+1, -1, -1):
            if i in h_cand and i in v_cand:
                return i**2
        return 1

    def get_candidate_len(self, cand, bars, removable_bars):
        for b in removable_bars:
            bars[b-1] = 0
            l, r = b-2, b
            while l >= 0 and bars[l] == 0:
                l -= 1
            while r < len(bars) and bars[r] == 0:
                r += 1
            cand.add(r-l)


# AC solution
# dig a little deeper, we don't need the variable hb and vb, even hBars and vBars are not needed
# we just need to find the max gap we can get from hBars and vBars
# with hBars, we can get a gap > 2 when there are continous removable bars
class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        h_max_gap = self.get_max_gap(hBars)
        v_max_gap = self.get_max_gap(vBars)
        return min(h_max_gap, v_max_gap)**2

    def get_max_gap(self, bars):
        result, curr = 1, 0
        bars.sort()
        for i in range(len(bars)):
            if i > 0 and bars[i] - bars[i-1] == 1:
                curr += 1
            else:
                curr = 2
            result = max(result, curr)
        return result