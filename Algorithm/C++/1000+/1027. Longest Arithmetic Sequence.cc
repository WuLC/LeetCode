/*
 * Created on Tue Apr 16 2019 12:56:34
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// two dimensional dp, O(n^2) time
// dp[i][j] represents the result ending at index i with diff j

#include <vector>
#include <unordered_map>

class Solution {
 public:
  int longestArithSeqLength(std::vector<int>& A) {
    std::unordered_map<int, std::unordered_map<int, int>> dp;
    int result = 0;
    for (int i = 0; i < A.size(); ++i) {
      dp[i] = unordered_map<int, int>{};
      for (int j = 0; j < i; ++j) {
        int diff = A[i] - A[j];
        dp[i][diff] = std::max(dp[i][diff], dp[j][diff] + 1);
        result = std::max(result, dp[i][diff]);
      }
    }
    return result + 1;
  }
};