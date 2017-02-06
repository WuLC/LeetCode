/**
* Author: WuLC
* Date:   2017-02-06 22:28:22
* Last modified by:   WuLC
* Last Modified time: 2017-02-06 22:31:08
* Email: liangchaowu5@gmail.com
*/

// simulate several steps, and the principle is that if n is magnification of 4, the first one to fetch the stone can not win
public class Solution {
    public boolean canWinNim(int n) {
        return n%4 != 0;
    }
}