#include <vector>
#include <string>

class Solution {
public:
    std::vector<int> minOperations(std::string boxes) {
        int n = boxes.size();
        std::vector<int> l_prefix(n, 0), r_prefix(n, 0);
        int i = 0, j = n-1, l_cnt=0, r_cnt=0;
        while (i<n || j>=0) {
            if (i < n) {
                if (i > 0) l_prefix[i] = l_prefix[i-1] + l_cnt;
                if (boxes[i] == '1') l_cnt++;
                i++;
            }
            if (j >= 0) {
                if (j < n-1) r_prefix[j] = r_prefix[j+1] + r_cnt;
                if (boxes[j] == '1') r_cnt++;
                j--;
            }
        }
        std::vector<int> result;
        result.reserve(n);
        for (int i = 0; i < n; i++) {
            result.push_back(l_prefix[i]+r_prefix[i]);
        }
        return result;
    }
};