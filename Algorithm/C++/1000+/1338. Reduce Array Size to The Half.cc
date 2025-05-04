#include <vector>
#include <unordered_map>
#include <utility>
#include <algorithm>

class Solution {
public:
    int minSetSize(std::vector<int>& arr) {
        std::unordered_map<int, int> counter;
        for (int a: arr) {
            counter[a]++;
        }
        std::vector<std::pair<int, int>> s_counter(counter.begin(), counter.end());
        sort(s_counter.begin(), s_counter.end(),
             [](const std::pair<int, int>& a, const std::pair<int, int>& b) {
                    return a.second > b.second;
             });

        int result = 0, tmp=0, n = arr.size();
        for (auto c: s_counter) {
            result += 1;
            tmp += c.second;
            if (tmp >= (n>>1)) break;
        }
        return result;
    }
};