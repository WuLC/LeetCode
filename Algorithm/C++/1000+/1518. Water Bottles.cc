class Solution {
public:
    int numWaterBottles(int numBottles, int numExchange) {
        int result = numBottles;
        int emptyBottles = numBottles;
        while (emptyBottles >= numExchange) {
            int exchanged = int(emptyBottles/numExchange);
            emptyBottles %= numExchange;
            emptyBottles += exchanged;
            result += exchanged;
        }
        return result;
    }
};
