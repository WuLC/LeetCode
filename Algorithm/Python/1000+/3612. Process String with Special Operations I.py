class Solution:
    def processStr(self, s: str) -> str:
        result = []
        for c in s:
            if c.isalpha():
                result.append(c)
            elif c == '*' and len(result) > 0:
                result.pop()
            elif c == '#':
                result += result
            elif c == '%':
                result = result[::-1]
        return ''.join(result)
        