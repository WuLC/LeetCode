/*
 * Created on Wed Feb 27 2019 20:53:54
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// record the number of lights at each row, column, left diagonal and right diagonal
// use hashmap instead of list to avoid memory limit exceeded
#include <vector>
#include <unordered_map>
#include <unordered_set>

using std::vector;
using std::unordered_map;

class Solution {
 public:
  vector<int> gridIllumination(int N, vector<vector<int>>& lamps, vector<vector<int>>& queries) {
    unordered_map<int, int> row, col, left_diagonal, right_diagonal;
    unordered_map<int, std::unordered_set<int>> source;
    for (auto e : lamps) {
      source[e[0]].insert(e[1]);
      row[e[0]]++;
      col[e[1]]++;
      left_diagonal[e[0]+e[1]]++;
      right_diagonal[e[0]-e[1]]++;
    }
    vector<int> result;
    for (auto q : queries) {
      if (row[q[0]] > 0 || col[q[1]] > 0 || left_diagonal[q[0]+q[1]] > 0 || right_diagonal[q[0]-q[1]] > 0) {
        result.push_back(1);
      } else {
        result.push_back(0);
      }
      for (int i = q[0]-1; i <= q[0]+1; ++i) {
        for (int j = q[1]-1; j <= q[1]+1; ++j) {
          if (source.count(i) > 0 && source[i].count(j) > 0) {
            row[i]--;
            col[j]--;
            left_diagonal[i+j]--;
            right_diagonal[i-j]--;            
          }
        }
      }
    }
    return result;
  }
};