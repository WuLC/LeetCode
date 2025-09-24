#include <vector>
#include <queue>
#include <utility>

class Solution {
public:
    double maxAverageRatio(std::vector<std::vector<int>>& classes, int extraStudents) {
        // by default priority_queue is max heap
        std::priority_queue<std::pair<double, int>> heap;
        int n = classes.size();
        for (int i = 0; i < n; i++) {
            heap.push(std::make_pair(gain(classes[i][0], classes[i][1]), i));
        }

        std::vector<int> counter(n, 0);
        while (extraStudents > 0) {
            int i = heap.top().second;
            counter[i]++;
            heap.pop();
            heap.push(std::make_pair(gain(classes[i][0]+counter[i], classes[i][1]+counter[i]), i));
            extraStudents--;
        }
        
        double result = 0;
        for (int i = 0; i < n; i++) {
            result += static_cast<double>(classes[i][0]+counter[i])/(classes[i][1]+counter[i]);
        }
        return result/n;
    }

private:
    double gain(int pass, int all) {
        return static_cast<double>(pass+1)/(all+1) - static_cast<double>(pass)/all;
    }
};