/**
* Author: WuLC
* Date:   2017-01-15 17:07:14
* Last modified by:   WuLC
* Last Modified time: 2017-01-15 17:08:47
* Email: liangchaowu5@gmail.com
*/


// compare target with the number on top right corner, and decide whether to delete the row or the column
public class Solution 
{
    public boolean searchMatrix(int[][] matrix, int target) 
    {
        int m = matrix.length;
        if (m==0) return false;
        int n = matrix[0].length;
        int row = 0,  col = n-1;
        while (row < m && col >= 0)
        {
            if (matrix[row][col] == target) return true;
            else if(matrix[row][col] < target) row++;
            else col--;
        }
        return false;
    }
}