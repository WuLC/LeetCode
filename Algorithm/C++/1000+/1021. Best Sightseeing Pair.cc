/*
 * Created on Fri Mar 29 2019 22:57:37
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// one pass solution, 
// find the max A[i]+i-j from left to right

#include <vector>


class Solution {
 public:
  int maxScoreSightseeingPair(std::vector<int>& A) {
    int result = 0, curr = A[0] - 1;
    for (int i = 1; i < A.size(); ++i) {
      result = std::max(result, curr + A[i]);
      curr = std::max(curr - 1, A[i] - 1);
    }
    return result;
  }
};