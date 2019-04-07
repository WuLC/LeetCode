/*
 * Created on Sun Apr 07 2019 20:44:19
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

 // bit manipulation

 import "strconv"

 func baseNeg2(N int) string {
	 if N == 0 {
		 return "0"
	 }
	 result := ""
	 idx, curr, carry := 0, 0, 0
	 for N > 0 || carry > 0 {
		 s := (N&1) + carry
		 curr, carry = s % 2, s / 2
		 result = strconv.Itoa(curr) + result
		 if (idx&1) > 0 && curr > 0 {
			 carry = 1
		 }
		 N >>= 1
		 idx++
	 }
	 return result	
 }