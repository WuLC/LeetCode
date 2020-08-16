#include <vector>

class Solution {
 public:
    bool threeConsecutiveOdds(std::vector<int>& arr) {
       int cnt=0;
       for(auto num: arr) {
           if (num&1 > 0) {
               cnt++;
               if (cnt==3) return true;
           } else {
               cnt = 0;
           }
       }
       return false;
    }
};