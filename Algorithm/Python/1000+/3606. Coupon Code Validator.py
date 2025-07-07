from collections import defaultdict

class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        bl = ["electronics", "grocery", "pharmacy", "restaurant"]
        record = defaultdict(list)
        for i in range(len(code)):
            if self.isLegalCode(code[i]) and businessLine[i] in bl and isActive[i]:
                record[businessLine[i]].append(code[i])

        result = []
        for b in bl:
            result += sorted(record[b])
        return result

    def isLegalCode(self, code):
        return len(code) > 0 and all(c.isalnum() or c == '_' for c in code)
        