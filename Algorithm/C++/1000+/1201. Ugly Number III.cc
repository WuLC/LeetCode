class Solution {
 public:
  int nthUglyNumber(int n, int A, int B, int C) {
    long a = long(A), b = long(B), c = long(C); // convert to long to avoid error when a*b
    long ab = (a*b)/gcd(a, b), bc = (b*c)/gcd(b, c), ac = (a*c)/gcd(a, c);
    long abc = (ab*c)/gcd(ab, c);
    int left = 1;
    long right = n * std::min(std::min(a, b), c), mid, k;
    while (left < right) {
        mid = left + ((right - left)>>1);
        k = mid/a + mid/b + mid/c - mid/ab - mid/bc - mid/ac + mid/abc;
        if (k < n) {
            left = mid + 1;
        } else {
            right = mid;
        }
    }
    return left;
  }
 
 private:
  int gcd(long n1, long n2) {
    if (n1 < n2) std::swap(n1, n2);
    while (n2 > 0) {
      int tmp = n2;
      n2 = n1 % n2;
      n1 = tmp;
    }
    return n1;
  }
};