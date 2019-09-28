#include <string>
#include <vector>
#include <unordered_map>

using std::string;
using std::vector;
using std::unordered_map;

class UnionFindSet {

 public:
  UnionFindSet(int n) {
    for (int i = 0; i < n; i++) {
      parent.push_back(i);
      depth.push_back(0);
    }
  }

  int findParent(int v) {
    if (parent[v] != v)
      parent[v] = findParent(parent[v]);
    return parent[v];
  }

  void unionNode (int v1, int v2) {
      int p1 = findParent(v1), p2 = findParent(v2);
      if (p1 == p2) return;
      if (depth[p1] > depth[p2]) {
        parent[p2] = p1;
      } else if (depth[p1] < depth[p2]) {
        parent[p1] = p2;
      } else {
        parent[p2] = p1;
        depth[p1]++;
      }
  }

  private:
   vector<int> parent, depth;
};

class Solution {
 public:
  string smallestStringWithSwaps(string s, vector<vector<int>>& pairs) {
    int n = s.length();
    UnionFindSet ufs(n);
    for (auto p: pairs) {
        ufs.unionNode(p[0], p[1]);
    }
    unordered_map<int, vector<int>> idxs;
    unordered_map<int, vector<char>> chars;
    vector<char> result;
    for (int i = 0; i < s.length(); i++) {
      int p = ufs.findParent(i);
      if (idxs.find(p) == idxs.end()) idxs[p] = vector<int> {};
      idxs[p].push_back(i);
      if (chars.find(p) == chars.end()) chars[p] = vector<char> {};
      chars[p].push_back(s[i]);
      result.push_back(s[i]);
    }
    for (auto p : idxs) {
      std::sort(idxs[p.first].begin(), idxs[p.first].end());
      std::sort(chars[p.first].begin(), chars[p.first].end());
      for (int i = 0; i < p.second.size(); i++) {
        result[p.second[i]] = chars[p.first][i];
      }
    }
    return string(result.begin(), result.end());
  }
};