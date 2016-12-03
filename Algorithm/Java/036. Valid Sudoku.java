/**
* Author: WuLC
* Date:   2016-12-03 19:44:43
* Last modified by:   WuLC
* Last Modified time: 2016-12-03 19:50:22
* Email: liangchaowu5@gmail.com
*/

// bit manipulation
public class Solution 
{
    public boolean isValidSudoku(char[][] board) 
    {
        int[] row = new int[9];
        int[] col = new int[9];
        int[][] block = new int[3][3];
        int num;
        for (int i = 0; i<9; i++)
        {
            for (int j=0; j<9; j++)
            {
                if (board[i][j] == '.') continue;
                if (board[i][j]>'9' || board[i][j]<'0') return false;
                num = board[i][j] - '0';
                // check row
                if ((row[i]&(1<<num)) != 0) return false;
                else row[i] ^= (1<<num);
                // check column
                if ((col[j]&(1<<num)) != 0) return false;
                else col[j] ^= (1<<num);
                // check block
                if ((block[i/3][j/3] & (1<<num)) != 0) return false;
                else block[i/3][j/3] ^= (1<<num);
                
                /* the above checking can be replaced by the followding code
                int tmp = 1<<num;
                if ( (row[i]&tmp)!=0 || (col[j]&tmp)!=0 || (block[i][j]&tmp)!= 0) return false;
                else
                {
                    row[i] ^= tmp;
                    col[j] ^= tmp;
                    block[i][j] ^= tmp;
                }
                 */
            }
        }
        return true;
    }
}