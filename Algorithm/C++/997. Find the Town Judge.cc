/*
 * Created on Mon Feb 25 2019 21:11:38
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// hashmap, simple solution
#include <vector>
#include <unordered_map>

using std::vector;
using std::unordered_map;

class Solution {
 public:
  int findJudge(int N, vector<vector<int>>& trust) {
    if (N == 1) return 1;
    int result = -1;
    unordered_map<int, int> count;
    for (auto t : trust) {
      count[t[1]]++;
      if (count[t[1]] == N-1) {
        if (result < 0) result = t[1];
        else return -1;
      }
    }

    for (auto t : trust) {
      if (t[0] == result) return -1;
    }
    return result;
  }
};