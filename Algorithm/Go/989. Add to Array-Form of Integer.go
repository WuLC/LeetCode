/*
 * Created on Sun Feb 10 2019 12:19:28
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

 // add bit by bit 
func addToArrayForm(A []int, K int) []int {
	result := []int{}
	idx := len(A) - 1
	carry, curr, sum := 0, 0, 0
	for idx >= 0 || K > 0 {
		if idx >= 0 && K > 0 {
			sum = A[idx] + (K % 10) + carry
		} else if idx >= 0{
			sum = A[idx] + carry
		} else {
			sum = (K % 10) + carry
		}
		carry, curr = sum / 10, sum % 10
		result = append(result, curr)
		idx--
		K /= 10
	}
    if carry > 0 {
        result = append(result, carry)
    }
	n := len(result)
	for i := 0; i < len(result)/2; i++ {
		result[i], result[n-i-1] = result[n-i-1], result[i]
	}
	return result
}