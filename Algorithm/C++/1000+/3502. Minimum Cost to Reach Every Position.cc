class Solution {
    public:
        vector<int> minCosts(vector<int>& cost) {
            int n = cost.size();
            std::vector<int> result;
            result.reserve(n);
            int prefix_min = 101;
            for (int i = 0; i < n; i++) {
                prefix_min = std::min(cost[i], prefix_min);
                result.push_back(prefix_min);
            }
            return result;
        }
    };