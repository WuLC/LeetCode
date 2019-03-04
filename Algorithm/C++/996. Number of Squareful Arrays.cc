/*
 * Created on Sun Mar 03 2019 23:11:14
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// graph, dfs with counter to deal with duplicate elements

#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <cmath>

class Solution {
 public:
  int numSquarefulPerms(std::vector<int>& A) {
    connection.clear();
    counter.clear();
    result = 0;
    for (int i = 0; i < A.size(); ++i) {
      counter[A[i]]++;
      for (int j = i+1; j < A.size(); ++j) {
        if (A[i]+A[j] == int(std::pow(int(std::sqrt(A[i]+A[j])), 2))) {
          connection[A[i]].insert(A[j]);
          connection[A[j]].insert(A[i]);
        }
      }
    }
    for (auto e : connection) {
      dfs(e.first, A.size() - 1);
    }
    return result;
  }

 private:
  std::unordered_map<int, std::unordered_set<int>> connection;
  std::unordered_map<int, int> counter;
  int result;
  void dfs(int curr, int left) {
    counter[curr]--;
    if (left == 0) result++;
    for (auto num : connection[curr]) {
      if (counter[num] > 0) {
        dfs(num, left-1);
      }
    }
    counter[curr]++;
  }
};