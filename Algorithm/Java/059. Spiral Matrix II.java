/**
* Author: WuLC
* Date:   2017-01-02 18:53:40
* Last modified by:   WuLC
* Last Modified time: 2017-01-02 20:24:09
* Email: liangchaowu5@gmail.com
*/

// set four directions beforehand, then just need one for loop
public class Solution 
{
    public int[][] generateMatrix(int n) 
    {
        int[][] matrix = new int[n][n];
        int[][] directions = {{0,1}, {1,0}, {0,-1}, {-1,0}};
        int currNum = 1, row = 0, col = 0;
        while (n>0)
        {
            if (n == 1) matrix[row][col] = currNum; // n is odd number
            for(int i=0;i<4;i++) // directions
            {
                for(int j=0; j<n-1; j++)
                {
                    matrix[row][col] = currNum;
                    currNum++;
                    row += directions[i][0];
                    col += directions[i][1];
                }
            }
            row += 1;
            col += 1;
            n -= 2;
        }
        return matrix;
    }
}