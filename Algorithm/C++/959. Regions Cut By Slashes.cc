/*
 * Created on Sun Dec 16 2018 20:19:22
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// dfs
#include <vector>
#include <string>

using std::vector;
using std::string;

class Solution {
 public:
  int regionsBySlashes(vector<string>& grid) {
    int n = 3 * grid.size();
    vector<vector<int>> mapping(n, vector<int>(n, 0));
    for (int i = 0; i < grid.size(); i++) {
      for (int j = 0; j < grid.size(); j++) {
        if (grid[i][j] == '/') {
          mapping[i*3][j*3+2] = 1;
          mapping[i*3+1][j*3+1] = 1;
          mapping[i*3+2][j*3] = 1;
        } else if (grid[i][j] == '\\') {
          mapping[i*3][j*3] = 1;
          mapping[i*3+1][j*3+1] = 1;
          mapping[i*3+2][j*3+2] = 1;
        }
      }
    }
    int count = 0;
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < n; j++) {
        if (mapping[i][j] == 0) {
          dfs(mapping, i, j, n);
          count++;
        }
      }
    }
    return count;
  }

 private:
  void dfs(vector<vector<int>>& mapping, int i, int j, int n) {
    if (i >= 0 && i < n && j >= 0 && j < n && mapping[i][j] == 0) {
      mapping[i][j] = -1;
      dfs(mapping, i - 1, j, n);
      dfs(mapping, i + 1, j, n);
      dfs(mapping, i, j - 1, n);
      dfs(mapping, i, j + 1, n);
    }
  }
};