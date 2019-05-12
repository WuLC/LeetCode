/*
 * Created on Sun May 12 2019 17:21:11
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// dp,O(n) time

#include <vector>

class Solution {
 public:
  int maxSumTwoNoOverlap(std::vector<int>& A, int L, int M) {
    return std::max(helper(A, L, M), helper(A, M, L));
  }

 private:
  int helper(std::vector<int>& A, int L, int M) {
    int n = A.size();
    std::vector<int> left(n+1, 0), right(n+1, 0);
    int curr_left = 0, curr_right = 0;
    for (int i = 0, j = n-1; i < n; i++, j--) {
      curr_left += A[i];
      curr_right += A[j];
      if (i >= L) curr_left -= A[i-L];
      if (j <= n-1-M) curr_right -= A[j+M];
      left[i+1] = std::max(left[i], curr_left);
      right[j] = std::max(right[j+1], curr_right);
    }
    int result = 0;
    for (int i = 0; i < n; i++) {
      result = std::max(result, std::max(left[i] + right[i], left[i+1] + right[i+1]));
    }
    return result;
  }
};