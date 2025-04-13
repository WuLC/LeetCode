#include <string>
#include <vector>

class Solution {
    public:
        int minimumBuckets(std::string hamsters) {
            int last_h = 0, h_count = 0;
            std::vector<int> gaps;
            for (int i = 0; i < hamsters.size(); i++) {
                if (hamsters[i] == 'H') {
                    h_count++;
                    if (h_count==1) {
                        gaps.push_back(i - last_h);
                    } else {
                        gaps.push_back(i - last_h - 1);
                    }
                    last_h = i;
                }
            }
            gaps.push_back(hamsters.size() - 1 - last_h);

            std::vector<bool> shared(gaps.size(), false);
            for (int i = 1; i < gaps.size(); i++) {
                if (gaps[i] == 0 && gaps[i-1] == 0) return -1;
                if (gaps[i] == 1 && !shared[i-1] && i != gaps.size() - 1) {
                    h_count--;
                    shared[i] = true;
                }
            }
            return h_count;
        }
    };