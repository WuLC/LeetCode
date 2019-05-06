/*
 * Created on Sun May 05 2019 22:26:48
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// bfs, record borders of connected component
#include <vector>
#include <queue>

using std::vector;
using std::queue;

class Solution {
 public:
  vector<vector<int>> colorBorder(vector<vector<int>>& grid, int r0, int c0, int color) {
    int m = grid.size(), n = grid[0].size();
    vector<vector<int>> visited(m, vector<int>(n, 0));
    vector<vector<int>> borders;
    queue<vector<int>> q;
    q.push(vector<int>{r0, c0});
    visited[r0][c0] = 1;
    vector<vector<int>> directions {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
    while (q.size() > 0) {
      vector<int> curr = q.front();
      q.pop();
      for (auto d : directions) {
        if (curr[0] == 0 || curr[0] == m - 1 || curr[1] == 0 || curr[1] == n - 1)
          borders.push_back(vector<int>{curr[0], curr[1]});
        int r = curr[0] + d[0], c = curr[1] + d[1];
        if (r >= 0 && r < m && c >= 0 && c < n) {
          if (grid[r][c] == grid[r0][c0]) {
            if (visited[r][c] == 0)
              q.push(vector<int>{r, c});
          } else {
            borders.push_back(vector<int>{curr[0], curr[1]});
          }
          visited[r][c] = 1;
        }
      }
    }
    for (auto b : borders) {
      grid[b[0]][b[1]] = color;
    }
    return grid;
  }
};