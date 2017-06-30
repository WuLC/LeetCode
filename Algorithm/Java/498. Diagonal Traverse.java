/*
* @Author: WuLC
* @Date:   2017-06-30 16:21:58
* @Last Modified by:   WuLC
* @Last Modified time: 2017-06-30 16:31:55
* @Email: liangchaowu5@gmail.com
*/


// decide the direction and starting position according to the sum of row index and column index
public class Solution
{
    public int[] findDiagonalOrder(int[][] matrix) 
    {
        if (matrix.length == 0) return new int[0];
        int m = matrix.length, n = matrix[0].length;
        int[] result = new int[m*n];
        int index = 0, row, col;
        for(int i = 0; i < m + n - 1; i++)
        {
            if( (i&1) == 1) // down
            {
                if (i < n) {row = 0; col = i;}
                else {row = i- n + 1; col = n-1;};
                while(col >= 0 && row < m)
                {
                    result[index] = matrix[row][col];
                    row++;
                    col--;
                    index++;
                }
            }
            else            // up
            {
                if (i < m) {row = i; col = 0;}
                else {row = m - 1; col = i - m + 1;};
                while(row >= 0 && col < n)
                {
                    result[index] = matrix[row][col];
                    row--;
                    col++;
                    index++;
                }
            }
        }
        return result;
    }
}