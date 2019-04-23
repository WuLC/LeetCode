/*
 * Created on Tue Apr 23 2019 21:4:17
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// bfs
#include <vector>
#include <queue>

using std::vector;

class Solution {
 public:
  vector<vector<int>> allCellsDistOrder(int R, int C, int r0, int c0) {
    vector<vector<int> visited(R, vector<int>(C)), result;
    std::queue<vector<int>> q;
    q.push(vector<int>{r0, c0});
    visited[r0][c0] = 1;
    vector<int> tmp;
    while (q.size() > 0) {
      tmp = q.front();
      result.push_back(tmp);
      int r = tmp[0], c = tmp[1];
      q.pop();
      if (r+1 < R && visited[r+1][c] == 0) {
        visited[r+1][c] = 1;
        q.push(vector<int>{r+1, c});
      }
      if (r-1 >=0 && visited[r-1][c] == 0) {
        visited[r-1][c] = 1;
        q.push(vector<int>{r-1, c});
      }
      if (c+1 < C && visited[r][c+1] == 0) {
        visited[r][c+1] = 1;
        q.push(vector<int>{r, c+1});
      }
      if (c-1 >= 0 && visited[r][c-1] == 0) {
        visited[r][c-1] = 1;
        q.push(vector<int>{r, c-1});
      }
    }
    return result;
  }
};
