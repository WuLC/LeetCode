/*
 * Created on Wed Oct 03 2018 10:48:50
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// greatest commom divisor
class Solution {
public:
    bool hasGroupsSizeX(vector<int>& deck) {
        unordered_map<int, int> count;
        for(int num:deck) count[num]++;
        int result = 0;
        for(auto iterator : count) result = __gcd(iterator.second, result);
        return result>1;
    }
};