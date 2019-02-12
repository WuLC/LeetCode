/*
 * Created on Sun Feb 10 2019 15:27:24
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// union find set
#include <vector>
#include <string>

using std::vector;
using std::string;

class Solution {
 public:
  bool equationsPossible(vector<string>& equations) {
    vector<int> parent;
    for (int i = 0; i < 26; i++) {
      parent.push_back(i);
    }
    vector<int> rank(26, 0);
    for (string e : equations) {
      if (e[1] == '=') {
        union_tree(int(e[0]) - 97, int(e[3]) - 97, parent, rank);
      }
    }

    for (string e : equations) {
      if (e[1] == '!' && find(int(e[0]) - 97, parent) == find(int(e[3]) - 97, parent)) {
        return false;
      }
    }
    return true;
  }

  int find(int v, vector<int>& parent) {
    if (parent[v] != v) {
      parent[v] = find(parent[v], parent);
    }
    return parent[v];
  }

  void union_tree(int v1, int v2, vector<int>& parent, vector<int>& rank) {
    int p1 = find(v1, parent), p2 = find(v2, parent);
    if (rank[p1] > rank[p2]) {
      parent[p2] = p1;
    } else if (rank[p1] < rank[p2]){
      parent[p1] = p2;
    } else {
      parent[p2] = p1;
      rank[p1]++;
    }
  }
};