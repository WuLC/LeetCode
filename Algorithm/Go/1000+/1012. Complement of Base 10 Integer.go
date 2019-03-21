/*
 * Created on Thu Mar 21 2019 9:38:43
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

 // bit manipulation
import "math"

func bitwiseComplement(N int) int {
	if N == 0 {
		return 1
	}
	count, n := 0, N
	for n > 0 {
		if (n & 1) == 1 {
			count++
		}
		n >>= 1
	}

	result, bit := 0, 0
	for count > 0 {
		if (N & 1) == 0 {
			result += int(math.Pow(float64(2), float64(bit)))
		} else {
			count--
		}
		bit++
		N >>= 1
	}
	return result
}

// second for loop can be written like this 
result := 0
var bit uint8 = 0 	// shift count type int, must be unsigned integer
for count > 0 {
	if (N & 1) == 0 {
		result += (1<<bit)
	} else {
		count--
	}
	bit++
	N >>= 1
}