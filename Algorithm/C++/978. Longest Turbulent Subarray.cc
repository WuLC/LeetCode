/*
 * Created on Wed Jan 23 2019 16:6:23
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// two pointers, O(n) time
#include <vector>

class Solution {
 public:
  int maxTurbulenceSize(std::vector<int>& A) {
    int result = 1;
    int left = 0, right = 1;
    while (right + 1 < A.size()) {
      if ((A[right] > A[right-1] && A[right] > A[right+1]) || (A[right] < A[right-1] && A[right] < A[right+1])) {
        right++;
      } else {
        if (A[right] != A[right-1]) result = std::max(result, right - left + 1);
        while (right < A.size() - 1 && A[right] == A[right + 1]) right++;
        left = right;
        right++;
      }
    }
    if (right < A.size() && A[right] != A[right-1]) result = std::max(result, right - left + 1);
    return result;
  }
};