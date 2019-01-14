/*
 * Created on Mon Jan 14 2019 20:28:8
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */
// priority queue with pair
#include <vector>
#include <queue>
#include <utility>

using std::vector;
using std::priority_queue;

class Solution {
 public:
  vector<vector<int>> kClosest(vector<vector<int>>& points, int K) {
    priority_queue<std::pair<int, vector<int>>> queue; // default max heap
    for (auto p : points) {
      queue.push(std::make_pair(p[0]*p[0] + p[1]*p[1], p));
      if (queue.size() > K) queue.pop();
    }
    vector<vector<int>> result;
    while (!queue.empty()) {
      result.push_back(queue.top().second);
      queue.pop();
    }
    return result;
  }
};