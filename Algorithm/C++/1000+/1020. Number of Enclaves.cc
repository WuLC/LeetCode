/*
 * Created on Mon Apr 01 2019 9:33:41
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

#include <vector>
#include <numeric>


class Solution {
 public:
  int numEnclaves(std::vector<std::vector<int>>& A) {
    int m = A.size(), n = A[0].size();
    for (int i = 0; i < m; ++i) {
      if (i == 0 || i == m-1) {
        for (int j = 0; j < n; ++j){
          if (A[i][j] == 1) dfs(A, i, j, m, n);
        }
      } else {
        if (A[i][0] == 1) dfs(A, i, 0, m, n);
        if (A[i][n-1] == 1) dfs(A, i, n-1, m, n);
      }
    }
    int result = 0;
    for (int i = 0; i < m; ++i) {
      result += std::accumulate(A[i].begin(), A[i].end(), 0);
    }
    return result;
  }

  void dfs(std::vector<std::vector<int>>& A, int i, int j, int m, int n) {
    A[i][j] = 0;
    if (i-1 >= 0 && A[i-1][j] == 1) dfs(A, i-1, j, m, n);
    if (i+1 < m && A[i+1][j] == 1) dfs(A, i+1, j, m, n);
    if (j-1 >= 0 && A[i][j-1] == 1) dfs(A, i, j-1, m, n);
    if (j+1 < n && A[i][j+1] == 1) dfs(A, i, j+1, m, n);
  }
};