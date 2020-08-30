#include <vector>
#include <algorithm>

class Solution {
public:
    bool containsPattern(std::vector<int>& arr, int m, int k) {
        for (auto start=arr.begin(); start < arr.end() - m*k + 1; start++) {
            // std::vector<int> sub(start, start+m); //slice vecor
            auto tmp = start;
            for(int i=0; i < k; i++) {
                if (!std::equal(start, start+m, tmp)) 
                    break;
                if (i==k-1) 
                    return true;
                tmp += m;
            }
        }        
        return false;
    }
};