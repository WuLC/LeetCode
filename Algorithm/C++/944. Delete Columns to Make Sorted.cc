/*
 * Created on Fri Nov 23 2018 20:56:19
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

class Solution {
 public:
  int minDeletionSize(vector<string>& A) {
    int m = A.size(), n = A[0].size();
    int count = 0;
    for (int i = 0; i < n; i++) {
      for (int j = 1; j < m; j++) {
        if (A[j][i] < A[j-1][i]) {
          count++;
          break;
        }
      }
    }
    return count;
  }
};