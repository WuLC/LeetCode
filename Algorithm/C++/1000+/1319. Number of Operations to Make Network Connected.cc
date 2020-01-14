/*
 * Created on Mon Jan 13 2020 10:08:31
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// dfs
#include <vector>
#include <unordered_map>
using std::vector;
using std::unordered_map;

class Solution {
public:
  int makeConnected(int n, vector<vector<int>>& connections) {
    if (connections.size() < n - 1) {
      return -1;
    }
    for (auto con: connections) {
      graph[con[0]].push_back(con[1]);
      graph[con[1]].push_back(con[0]);
    }
    for (int i = 0; i < n; i++) {
      visited.push_back(0);
    }
    int result = 0;
    for (int i = 0; i < n; i++) {
      result += dfs(i);
    }
    return result - 1;
  }
private:
  int dfs(int i) {
    if (visited[i] == 1)  return 0;
    visited[i] = 1;
    for (auto j : graph[i]) {
      if (visited[j] == 1) continue;
      dfs(j);
    }
    return 1;
  }

  unordered_map<int, vector<int>> graph;
  vector<int> visited;
};

