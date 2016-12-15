/**
* Author: WuLC
* Date:   2016-12-15 20:26:28
* Last modified by:   WuLC
* Last Modified time: 2016-12-15 20:28:36
* Email: liangchaowu5@gmail.com
*/

// O(1) space, O(n^2) time
// swap matrix[i][:] with matrix[n-i-1][:], then transpose the matrix
public class Solution 
{
    public void rotate(int[][] matrix)
    {
        int n = matrix.length;
         int tmp;
        // swap matrix[i][:] with matrix[n-i-1][:]
        for(int row = 0; row < n/2; row++)
        {
            for(int col = 0; col<n; col++)
            {
                // swap
                tmp = matrix[row][col];
                matrix[row][col] = matrix[n-1-row][col];
                matrix[n-1-row][col] = tmp;
            }
        }
        // transpose the matrix
        for(int row = 0; row < n; row++)
        {
            for (int col = row+1; col < n; col++)
            {
                tmp = matrix[row][col];
                matrix[row][col] = matrix[col][row];
                matrix[col][row] = tmp;
            }
        }
    }
}