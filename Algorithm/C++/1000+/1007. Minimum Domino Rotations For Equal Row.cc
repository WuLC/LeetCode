/*
 * Created on Fri Mar 15 2019 17:30:21
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// simple solution, O(n) time

#include <vector>


class Solution {
 public:
  int minDominoRotations(std::vector<int>& A, std::vector<int>& B) {
      int a = minSwap(A[0], A, B), b = minSwap(B[0], A, B);
      if (a == -1) {
        return b;
      } else if (b == -1) {
        return a;
      } else {
        return std::min(a, b);
      }
  }

  int minSwap(int target, std::vector<int>& A, std::vector<int>& B) {
    int num_A = 0, num_B = 0;
    for (int i = 0; i < A.size(); ++i) {
      if (A[i] != target && B[i] != target)
        return -1;
      if (A[i] != target)
        ++num_A;
      if (B[i] != target)
        ++num_B;
    }
    return std::min(num_A, num_B);
  }
};