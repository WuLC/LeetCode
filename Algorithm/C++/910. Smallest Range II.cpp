/*
 * Created on Mon Sep 24 2018 12:16:26
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// sort, add K for the smaller part and minus K for the larger part
class Solution {
public:
    int smallestRangeII(vector<int>& A, int K) {
        std::sort(A.begin(), A.end());
        int result = A.back() - A[0];
        for(int i=0; i<A.size()-1; i++){
            int tmp = std::max(A[i]+K, A.back()-K) - std::min(A[0]+K, A[i+1]-K);
            result = std::min(result, tmp);
        }
        return result;
    }
};