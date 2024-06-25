#include <vector>
#include <algorithm>

class Solution {
public:
    std::vector<int> colorTheArray(int n, std::vector<std::vector<int>>& queries) {
        std::vector<int> result;
        std::vector<int> colors(n, 0);
        int idx, color, cnt=0;
        for (auto q: queries) {
            idx = q[0];
            color = q[1];
            std::vector<int> neighbor{idx-1, idx+1};
            for (auto i: neighbor) {
                if (i >=0 && i < n) {
                    if (colors[i] != 0 && colors[i] == colors[idx]) cnt--;
                    if (color == colors[i]) cnt++;
                }
            };
            colors[idx] = color;
            result.push_back(cnt); 
        };   
        return result;
    }
};