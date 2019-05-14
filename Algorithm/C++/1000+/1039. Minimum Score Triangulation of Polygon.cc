/*
 * Created on Tue May 14 2019 19:43:12
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */


//recursive
#include <vector>

using std::vector;


class Solution {
 public:
  int minScoreTriangulation(vector<int>& A) {
    int n = A.size();
    vector<vector<int>> dp(n, vector<int>(n, 0));
    return helper(A, 0, n-1, dp); 
  }

 private:
  int helper(vector<int>& A, int i, int j, vector<vector<int>>& dp) {
    for (int k = i + 1; k < j; k++) {
      if (dp[i][k] == 0) dp[i][k] = helper(A, i, k, dp);
      if (dp[k][j] == 0) dp[k][j] = helper(A, k, j, dp);
      int tmp = dp[i][k] + A[i] * A[j] * A[k] + dp[k][j];
      if (dp[i][j] == 0)
        dp[i][j] = tmp;
      else
        dp[i][j] = std::min(dp[i][j], tmp);
    }
    return dp[i][j];
  }
};