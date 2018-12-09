/*
 * Created on Sun Dec 09 2018 9:34:24
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// union find set

#include <vector>
#include <set>
#include <unordered_map>

using std::vector;
using std::set;
using std::unordered_map;

// solution 1, assign each stone a number and connect them
class Solution1 {
 public:
  int removeStones(vector<vector<int>>& stones) {
    // construct edges
    unordered_map<int, vector<int>> row_index, col_index;
    for(int i = 0; i < stones.size(); i++) {
      row_index[stones[i][0]].push_back(i);
      col_index[stones[i][1]].push_back(i);
    }
    vector<vector<int>> edges;
    for (auto m : row_index) {
      for (int i = 0; i < m.second.size(); i++) {
        for (int j = i+1; j < m.second.size(); j++) {
          edges.push_back(vector<int>{m.second[i], m.second[j]});
        }
      }
    }
    for (auto m : col_index) {
      for (int i = 0; i < m.second.size(); i++) {
        for (int j = i+1; j < m.second.size(); j++) {
          edges.push_back(vector<int>{m.second[i], m.second[j]});
        }
      }
    }

    // union find
    vector<int> parents(stones.size()), rank(stones.size());
    std::iota(parents.begin(), parents.end(), 0); // C++ 11
    std::fill(rank.begin(), rank.end(), 0);
    for(auto e : edges) 
      Union(e[0], e[1], parents, rank);

    // count the number of unique parents
    set<int> unique_parents;
    for(int i = 0; i < stones.size(); i++)
      unique_parents.insert(Find(i, parents));
    return stones.size() - unique_parents.size();
  }

 private:
  int Find(int val, vector<int>& parents) {
    if (parents[val] != val) {
      parents[val] = Find(parents[val], parents);
    }
    return parents[val];
  }

  void Union(int v1, int v2, vector<int>& parents, vector<int>& rank) {
    int p1 = Find(v1, parents), p2 = Find(v2, parents);
    if (p1 == p2)
      return;
    else if(rank[p1] > rank[p2])
      parents[p2] = p1;
    else if(rank[p1] < rank[p2])
      parents[p1] = p2; 
    else {
      parents[p2] = p1;
      rank[p1]++;
    }
  }
};

// solution 2, simpler, connect the row index and column index of the stones
class Solution2 {
 public:
  int removeStones(vector<vector<int>>& stones) {

  }
};