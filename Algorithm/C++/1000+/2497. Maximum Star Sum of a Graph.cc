#include <queue>
#include <vector>
#include <unordered_map>
#include <algorithm> 

class Solution {
public:
    int maxStarSum(std::vector<int>& vals, std::vector<std::vector<int>>& edges, int k) {
        std::unordered_map<int, std::vector<int>> neighbors;
        for (auto& edge: edges) {
            if (vals[edge[1]] > 0) {
                neighbors[edge[0]].push_back(vals[edge[1]]);
            }
            if (vals[edge[0]] > 0) {
                neighbors[edge[1]].push_back(vals[edge[0]]);
            }
        }

        int result = *std::max_element(vals.begin(), vals.end());
        for(auto& _pair: neighbors) {
            std::priority_queue pq(_pair.second.begin(), _pair.second.end()); // 默认是 max heap
            int sum=vals[_pair.first], count = 0;
            while(!pq.empty() && count < k) {
                sum += pq.top();
                pq.pop();
                count++;
            }
            result = std::max(result, sum);
        }
        return result;
    }
};