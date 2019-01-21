/*
 * Created on Sun Jan 20 2019 18:22:36
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// O(n) time, O(n) space
#include <vector>
#include <cmath>

using std::vector;

class Solution {
 public:
  vector<int> sortedSquares(vector<int>& A) {
    int idx = A.size();
    for (int i = 0; i < A.size(); ++i) {
      if (A[i] >= 0) {
       idx = i;
       break;
      }
    }
    vector<int> result;
    int left = idx - 1, right = idx;
    while (left >= 0 && right < A.size()) {
      if (std::abs(A[left]) > std::abs(A[right])) {
        result.push_back(A[right] * A[right]);
        right++;
      } else {
        result.push_back(A[left] * A[left]);
        left--;        
      }
    }
    while (left >= 0) {
      result.push_back(A[left] * A[left]);
      left--;       
    }
    while (right < A.size()) {
      result.push_back(A[right] * A[right]);
      right++;      
    }
    return result;
  }
};