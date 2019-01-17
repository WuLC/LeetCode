/*
 * Created on Thu Jan 17 2019 9:28:18
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// prefix sum with counter of different mod result
#include <vector>

using std::vector;

class Solution {
 public:
  int subarraysDivByK(vector<int>& A, int K) {
    vector<int> mod_count(K, 0);
    mod_count[0] = 1;
    int prefix = 0, result = 0;
    for (auto num : A) {
      prefix = (prefix + num) % K;
      if (prefix < 0) prefix += K;
      result += mod_count[prefix];
      mod_count[prefix]++;
    }
    return result;
  }
};