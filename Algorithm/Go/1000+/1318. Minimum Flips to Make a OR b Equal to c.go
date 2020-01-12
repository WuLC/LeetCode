/*
 * Created on Sun Jan 12 2020 15:38:50
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

 func minFlips(a int, b int, c int) int {
    result := 0
    for a > 0 || b > 0 || c > 0 {
        lastBit := c&1
        if lastBit == 1 && (a&1) == 0 && (b&1) == 0 {
            result++
        } else if lastBit == 0 && ((a&1) == 1 || (b&1) == 1) {
            result += a&1
            result += b&1
        }
        a >>= 1
        b >>= 1
        c >>= 1
    }
    return result
}     