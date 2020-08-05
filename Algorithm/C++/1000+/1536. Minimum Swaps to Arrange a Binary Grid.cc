#include <vector>

class Solution {
public:
    int minSwaps(std::vector<std::vector<int>>& grid) {
        std::vector<int> zeroCnt;
        int n = grid.size();
        for(int i=0; i<n; i++) {
            zeroCnt.push_back(getZeroCnt(grid[i]));
        }
        int result = 0;
        // greedy
        for(int i = 0; i < n; i++) {
            if (zeroCnt[i] >= n-i-1) continue;
            else {
                int j = i+1;
                while (j < n && zeroCnt[j] < n-i-1) j++;
                if (j == n) return -1;
                result += j-i;
                while(j > i) {
                    std::swap(zeroCnt[j], zeroCnt[j-1]);
                    j--;
                }
            }
        }
        return result;
    }

private:
    int getZeroCnt(std::vector<int>& arr) {
        int result = 0;
        for(auto it=arr.rbegin(); it != arr.rend(); it++) {
            if ((*it) == 0) result++;
            else break;
        }
        return result;
    }
};