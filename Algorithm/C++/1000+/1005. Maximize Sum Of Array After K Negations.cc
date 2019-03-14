/*
 * Created on Thu Mar 14 2019 21:59:32
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

#include <vector>

class Solution {
 public:
  int largestSumAfterKNegations(std::vector<int>& A, int K) {
    std::sort(A.begin(), A.end());
    int idx = -1;
    for (int i = 0; i < A.size(); ++i) {
      if (A[i] >= 0) {
        idx = i;
        break;
      }
    }
    int result = 0;
    if (idx < 0 || idx >= K) {
      for (auto num : A) {
        if (K > 0) {
          result += -1*num;
          K--;
        } else {
          result += num;
        }
      }
    } else {
      int left = (K-idx)&1;
      for (int i = 0; i < A.size(); ++i) {
        if (i == idx && left > 0) {
          if (i > 0 && -1*A[i-1] < A[i])
            result += 2*A[i-1];
          else
            result += -2*A[i];
          left--;
        }
        result += A[i]<0? -1*A[i]: A[i];
      }
    }
    return result;
  }
};