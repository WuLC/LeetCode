/*
 * Created on Thu Mar 07 2019 17:4:38
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

//two pointers, O(n) time, O(1) space
#include <vector>

class Solution {
 public:
  int longestOnes(std::vector<int>& A, int K) {
    int left = 0, right = 0, result = 0;
    while (right < A.size()) {
      if (A[right] == 0) K--;
      while (K < 0) {
        if (A[left] == 0) K++;
        left++;
      }
      result = std::max(result, right-left+1);
      right++;
    }
    return result;
  }
};