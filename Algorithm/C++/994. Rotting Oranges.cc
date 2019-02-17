/*
 * Created on Sun Feb 17 2019 19:46:25
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// bfs, there may be multiple rotton oranges
#include <vector>
#include <queue>

using std::vector;
using std::queue;

class Solution {
 public:
  int orangesRotting(vector<vector<int>>& grid) {
    queue<vector<int>> q;
    int m = grid.size(), n = grid[0].size();
    for (int i = 0; i < m; ++i) {
      for (int j = 0; j < n; ++j) {
        if (grid[i][j] == 2)
          q.push(vector<int>{i, j, 0});
      }
    }
    int result = 0;
    vector<vector<int>> directions = {{-1, 0}, {1, 0}, {0, 1}, {0, -1}};
    while (q.size() > 0) {
      vector<int> curr = q.front();
      q.pop();
      result = curr[2];
      for (auto d : directions) {
        int ni = curr[0] + d[0], nj = curr[1] + d[1];
        if (ni >= 0 && ni < m && nj >=0 && nj < n && grid[ni][nj] == 1) {
          grid[ni][nj] = 2;
          q.push(vector<int>{ni, nj, curr[2]+1});
        }
      }
    }
    for (int i = 0; i < m; ++i) {
      for (int j = 0; j < n; ++j) {
        if (grid[i][j] == 1) return -1;
      }
    }
    return result;
  }
};