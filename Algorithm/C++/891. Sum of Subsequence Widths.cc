/*
 * Created on Sat Dec 29 2018 16:50:10
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// be careful of overflow
#include <vector>

using std::vector;

class Solution {
 public:
  int sumSubseqWidths(vector<int> A) {
    std::sort(A.begin(), A.end());
    long c = 1, result = 0, mod = 1e9 + 7;
    for (int i = 0; i < A.size(); ++i, c = (c << 1) % mod)
      result = (result + A[i] * c - A[A.size() - i - 1] * c) % mod;
    return (result + mod) % mod;
  }
};