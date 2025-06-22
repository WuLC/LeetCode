class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        s_fill = ""
        if len(s)%k > 0:
            s_fill = fill*(k-(len(s)%k))
        s += s_fill
        return [s[i:i+k] for i in range(0, len(s), k)]