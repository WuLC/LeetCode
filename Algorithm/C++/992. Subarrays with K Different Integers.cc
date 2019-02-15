/*
 * Created on Fri Feb 15 2019 14:4:30
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// two pointers
#include <vector>
#include <unordered_map>

class Solution {
 public:
  int subarraysWithKDistinct(std::vector<int>& A, int K) {
    int i = 0, j = 0, prefix = 0, result = 0;
    unordered_map<int, int> count;
    while (j < A.size()) {
      count[A[j]] += 1;
      j++;
      while (count.size() > K) {
        prefix = 0;
        count[A[i]]--;
        if (count[A[i]] == 0) count.erase(A[i]);
        i++;
      }
      if (count.size() == K){
        result++;
        while (count[A[i]] > 1) {
          count[A[i]]--;
          prefix++;
          i++;
        }
      }
      result += prefix;
    }
    return result;
  }
};