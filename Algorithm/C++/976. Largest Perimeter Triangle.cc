/*
 * Created on Mon Jan 14 2019 20:53:37
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// triangle with edges a, b, c is legal only when 
// a+b > c
// a+c > b
// b+c > a

#include <vector>
#include <algorithm>

using std::vector;

class Solution {
 public:
  int largestPerimeter(vector<int>& A) {
    std::sort(A.begin(), A.end());
    int result = 0;
    for (int i = A.size() - 1; i > 1; i--) {
      if (A[i] < A[i-1] + A[i-2]) {
        result = A[i] + A[i-1] + A[i-2];
        break;
      }
    }
    return result;
  }
};