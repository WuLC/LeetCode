/**
* Author: WuLC
* Date:   2016-12-30 21:29:02
* Last modified by:   WuLC
* Last Modified time: 2016-12-30 21:29:58
* Email: liangchaowu5@gmail.com
*/


// use four pointers to represent current unvisited area
// pay attention to the case when there is only one row or one column
public class Solution 
{
    public List<Integer> spiralOrder(int[][] matrix) 
    {
        List<Integer> result = new ArrayList<Integer>();
        if (matrix.length == 0) return result;
        int m = matrix.length, n = matrix[0].length;
        int upRow = 0, downRow = m-1, leftCol = 0, rightCol = n-1;
        while (upRow <= downRow && leftCol <= rightCol)
        {
            for (int i=leftCol; i <= rightCol; i++)  result.add(matrix[upRow][i]);
            upRow++;
            for (int i=upRow; i <=downRow; i++) result.add(matrix[i][rightCol]);
            rightCol--;
            if (upRow <= downRow)  // avoid final row duplicate
            {
                for (int i=rightCol; i >= leftCol; i--) result.add(matrix[downRow][i]);
                downRow--;
            }
            if (leftCol <= rightCol)  // avoid final col duplicate
            {
                for(int i=downRow; i>=upRow; i--) result.add(matrix[i][leftCol]);
                leftCol++;
            }
        }
        return result;
    }
}