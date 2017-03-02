/**
* Author: LC
* Date:   2017-02-22 21:34:53
* Last modified by:   WuLC
* Last Modified time: 2017-02-22 21:37:11
* Email: liangchaowu5@gmail.com
*/


// store the index of zero column in the first row and the index of zero row in the first column
// pay attention that first column should not be traversed and just use a variable to represent it
public class Solution 
{
    public void setZeroes(int[][] matrix) 
    {
        if (matrix.length == 0) return;
        int m = matrix.length, n = matrix[0].length;
        int col0 = 1;
        for(int i=0; i<m; i++)
        {
            if(matrix[i][0] == 0) col0 = 0;
            for(int j=1; j<n; j++)
            {
                if (matrix[i][j] == 0)
                {
                    matrix[i][0] = matrix[0][j] = 0;
                }
            }
        }
        
        for(int i = m-1; i >= 0; i--)
        {
            for(int j=1; j<n; j++)
            {
                if (matrix[i][0] == 0 || matrix[0][j] == 0)
                    matrix[i][j] = 0;
            }
            if (col0 == 0) matrix[i][0] = 0;
        }
        
    }
}