#include <vector>

class Solution {
    public:
        int maximizeSquareHoleArea(int n, int m, std::vector<int>& hBars, std::vector<int>& vBars) {
            int maxGap = std::min(getMaxGap(hBars), getMaxGap(vBars));
            return maxGap*maxGap;
        }

    private:
        int getMaxGap(std::vector<int>& bars) {
            int result = 1, curr = 0;
            std::sort(bars.begin(), bars.end());
            for (int i = 0; i < bars.size(); i++) {
                if (i > 0 && bars[i] - bars[i-1] == 1) {
                    curr++;
                } else {
                    curr = 2;
                }
                result = std::max(result, curr);
            }
            return result;
        }
    };