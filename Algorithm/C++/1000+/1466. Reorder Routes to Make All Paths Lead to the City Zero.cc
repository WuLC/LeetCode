#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <queue>

class Solution {
  public:
    int minReorder(int n, std::vector<std::vector<int>>& connections) {
        std::unordered_map<int, std::unordered_set<int>> direction, neighbor;
        std::unordered_set<int> visited;
        std::queue<int> q;
        int result = 0;
        q.push(0);
        for(auto conn: connections) {
            direction[conn[0]].insert(conn[1]);
            neighbor[conn[0]].insert(conn[1]);
            neighbor[conn[1]].insert(conn[0]);
        }
        while (q.size() > 0) {
            int curr = q.front();
            visited.insert(curr);
            q.pop();
            for (int node: neighbor[curr]) {
                if (visited.count(node) != 0) continue;
                if (direction[node].count(curr) == 0) result++;
                q.push(node);
                
            }
        }
        return result;
    }
};