/*
 * Created on Wed Dec 19 2018 14:27:15
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// greedy
#include <vector>
#include <string>

using std::vector;
using std::string;

class Solution {
 public:
  int minDeletionSize(vector<string>& A) {
    int m = A.size(), n = A[0].size();
    vector<bool> sorted(m - 1, false);
    int count = 0;
    for (int i = 0; i < n; i++) {
      bool legal = true;
      for (int j = 0; j < m - 1; j++) {
        if (!sorted[j] && A[j][i] > A[j+1][i]) {
          count++;
          legal = false;
          break;
        }
      }
      if (legal) {
        for (int j = 0; j < m - 1; j++) {
          if (A[j][i] < A[j+1][i]) {
            sorted[j] = true;
          }
        }
      }
    }
  return count;
  }
};