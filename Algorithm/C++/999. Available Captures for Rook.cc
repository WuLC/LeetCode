/*
 * Created on Thu Feb 28 2019 8:42:44
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// simple solution
#include <vector>

using std::vector;

class Solution {
 public:
  int numRookCaptures(vector<vector<char>>& board) {
      int result = 0;
      for (int i = 0; i < 8; ++i) {
        for (int j = 0; j < 8; ++j) {
          if (board[i][j] == 'R') {
            vector<vector<int>> directions{{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
            for (auto d : directions) {
              int ni = i, nj = j;
              while (ni+d[0] >= 0 && ni+d[0] < 8 && nj+d[1] >= 0 && nj+d[1] < 8) {
                ni += d[0];
                nj += d[1];
                if (board[ni][nj] == 'p') {
                  result++;
                  break;
                } else if (board[ni][nj] == 'B') {
                  break;
                }
              }
            }
          return result;
          }
        }
      }
    return result;
  }
};