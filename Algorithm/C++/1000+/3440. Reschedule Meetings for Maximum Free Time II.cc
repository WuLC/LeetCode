#include <vector>
class Solution {
public:
    int maxFreeTime(int eventTime, std::vector<int>& startTime, std::vector<int>& endTime) {
        int n = startTime.size();
        std::vector<int> free_time;
        free_time.reserve(n+1);
        for (int i = 0; i < n-1; i++) {
            if (i == 0) {
                free_time.push_back(startTime[0]);
            }
            free_time.push_back(startTime[i+1] - endTime[i]);
        }
        free_time.push_back(eventTime - endTime[n-1]);

        std::vector<int> largest_left(n, 0), largest_right(n, 0);
        for (int i = 1; i < n; i++) {
            largest_left[i] = std::max(largest_left[i-1], free_time[i-1]);
        }
        for (int i = n-2; i >= 0; i--) {
            largest_right[i] = std::max(largest_right[i+1], free_time[i+2]);
        }

        int interval, result = 0;
        for (int i = 0; i < n; i++) {
            result = std::max(result, free_time[i] + free_time[i+1]);
            interval = endTime[i] - startTime[i];
            if (largest_left[i] >= interval || largest_right[i] >= interval) {
                result = std::max(result, free_time[i] + free_time[i+1] + interval);
            }
        }
        return result;
    }
};