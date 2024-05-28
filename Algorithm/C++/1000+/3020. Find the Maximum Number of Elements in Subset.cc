#include <vector>
#include <algorithm>
#include <unordered_map>

class Solution {
public:
    int maximumLength(std::vector<int>& nums) {
        std::sort(nums.begin(), nums.end());
        std::unordered_map<long, long> counter;
        for (auto num: nums) {
            if (counter.find(num) != counter.end()) {
                counter[num]++;
            } else {
                counter[num] = 1;
            }
        }

        int result = 1;
        long next_num = 0;
        for (long num: nums) {
            next_num = num*num;
            if (next_num > nums[nums.size()-1]) break; //early stop
            
            int cnt=0;
            while (counter.find(num) != counter.end() && counter[num] > 0) {
                if (counter[num] >= 2 &&
                    counter.find(next_num) != counter.end() &&
                    counter[next_num] > 0) {
                        counter[num] -= 2;
                        cnt += 2;
                    } else {
                        cnt += 1;
                        break;
                    }
                num = next_num;
                next_num = num*num;
            }
            result = std::max(result, cnt);
        }
        if ((result&1) == 0) result--; 
        return result;
    }
};