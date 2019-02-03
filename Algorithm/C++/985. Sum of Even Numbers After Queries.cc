/*
 * Created on Sun Feb 03 2019 17:35:26
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// simple solution
#include <vector>

using std::vector;

class Solution {
 public:
  vector<int> sumEvenAfterQueries(vector<int>& A, vector<vector<int>>& queries) {
    vector<int> result;
    int tmp = 0;
    for (auto num : A) {
      if ((num&1) == 0) {
        tmp += num;
      }
    }
    for (auto q : queries) {
      if ((A[q[1]]&1) == 0 && (q[0]&1) == 0)
          tmp += q[0];
      else if ((A[q[1]]&1) == 1 && (q[0]&1) == 1)
          tmp += A[q[1]] + q[0];
      else if ((A[q[1]]&1) == 0 && (q[0]&1) == 1)
          tmp -= A[q[1]];
      result.push_back(tmp);
      A[q[1]] += q[0];
    }
    return result;
  }
};