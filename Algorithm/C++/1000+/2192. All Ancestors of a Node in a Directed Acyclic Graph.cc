#include <vector>
#include <unordered_set>
#include <unordered_map>

class Solution {
public:
    vector<vector<int>> getAncestors(int n, vector<vector<int>>& edges) {
        graph.clear();
        result = std::vector<std::vector<int>>(n);
        for (auto e: edges) {
            if (graph.find(e[0]) == graph.end()) {
                graph[e[0]] = std::vector<int>();
            }
            graph[e[0]].push_back(e[1]);
        }
        for(int i = 0; i < n; i++) {
            std::unordered_set<int> visited;
            dfs(i, i, visited);
        }
        return result;
    }

private:
    void dfs(int parent, int curr, std::unordered_set<int>& visited) {
        if (parent != curr) {
            result[curr].push_back(parent);
        }
        if (graph.find(curr) != graph.end()) {
            for (int neigh: graph[curr]) {
                if (visited.find(neigh) == visited.end()) {
                    visited.insert(neigh);
                    dfs(parent, neigh, visited);
                }
            }
        }
    }
    std::unordered_map<int, std::vector<int>> graph;
    std::vector<std::vector<int>> result;

};