class Solution(object):
    def nthUglyNumber(self, n, a, b, c):
        """
        :type n: int
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        def gcd(n1, n2):
            if n1 < n2:
                n1, n2 = n2, n1
            while n2 != 0:
                n1, n2 = n2, n1%n2
            return n1
        ab, bc, ac = (a * b)/gcd(a, b), (b * c)/gcd(b, c), (a * c)/gcd(a, c)
        abc = (ab * c)/gcd(ab, c)
        left, right = 1, n * min([a, b, c])
        while left < right:
            mid = left + ((right - left)>>1)
            k = mid/a + mid/b + mid/c - mid/ab - mid/bc - mid/ac + mid/abc
            if k < n:
                left = mid + 1
            else:
                right = mid
        return left