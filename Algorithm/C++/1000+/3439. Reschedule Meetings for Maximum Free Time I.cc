#include <vector>

class Solution {
public:
    int maxFreeTime(int eventTime, int k, vector<int>& startTime, vector<int>& endTime) {
        int n = startTime.size();
        std::vector<int> free_time;
        free_time.reserve(n+1);

        for (int i = 0; i < n - 1; i++) {
            if (i == 0) {
                free_time.push_back(startTime[i]);
            }
            free_time.push_back(startTime[i+1] - endTime[i]);
        }
        free_time.push_back(eventTime - endTime[n-1]);

        int left = 0, right = 0;
        int tmp = 0, result = 0;
        while (right < free_time.size()) {
            tmp += free_time[right];
            if (right - left == k) {
                result = std::max(result, tmp);
                tmp -= free_time[left++];
            }
            right++;
        }
        return result;
    }
};