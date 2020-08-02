#include <vector>

class Solution {
public:
    int getWinner(std::vector<int>& arr, int k) {
        int cnt = 0, curr_num = arr[0];
        for(int i=1; i<arr.size(); i++) {
            if(curr_num < arr[i]) {
                cnt = 1;
                curr_num = arr[i];
            } else {
                cnt++;
            }
            if (cnt == k) break;
        }
        return curr_num;
    }
};