/*
 * Created on Wed Oct 03 2018 16:30:29
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// O(n) time
class Solution {
public:
    int partitionDisjoint(vector<int>& A) {
        int idx = 0, left_max = A[0], curr_max = A[0];
        for(int i = 1; i < A.size(); i++) {
            if(left_max > A[i]) {
                left_max = curr_max;
                idx = i;
            }
            else curr_max = std::max(curr_max, A[i]);
        }
        return idx+1;
    }
};