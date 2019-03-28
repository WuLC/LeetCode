/*
 * Created on Thu Mar 28 2019 23:33:46
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

#include <vector>
#include <numeric>

class Solution {
 public:
  bool canThreePartsEqualSum(std::vector<int>& A) {
    int sum = std::accumulate(A.begin(), A.end(), 0);
    if (sum % 3 != 0) return false;
    int ave = sum/3;
    int count = 0, tmp = 0;
    for (auto num : A) {
      if (tmp == ave) {
        count++;
        tmp = 0;
      }
      tmp += num;
    }
    if (tmp == ave) count++;
    return count==3;
  }
};