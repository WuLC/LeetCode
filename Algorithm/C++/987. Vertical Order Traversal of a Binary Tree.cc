/*
 * Created on Tue Feb 05 2019 17:47:18
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */


// hashtable with priority queue
#include <vector>
#include <map>
#include <queue>

using std::vector;
using std::map;
using std::priority_queue;
using std::pair;

class Solution {
 public:
  vector<vector<int>> verticalTraversal(TreeNode* root) {
    record.clear();
    dfs(root, 0, 0);
    vector<vector<int>> result;
    for (auto r : record) {
      vector<int> tmp;
      auto q = r.second;
      while (!q.empty()) {
        tmp.push_back(-1 * q.top().second);
        q.pop();
      }
      result.push_back(tmp);
    }
    return result;
  }

  void dfs(TreeNode* root, int x, int y) {
    if (root == nullptr) return;
    if (record.count(x) == 0) record[x] = priority_queue<pair<int, int>>{};
    record[x].push(std::make_pair(y, -1 * root->val));
    dfs(root->right, x+1, y-1);
    dfs(root->left, x-1, y-1);
  }

 private:
    map<int, priority_queue<pair<int, int>>> record;  
};