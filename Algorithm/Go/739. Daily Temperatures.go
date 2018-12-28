/*
 * Created on Fri Dec 28 2018 13:51:28
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// stack, O(n) time
func dailyTemperatures(T []int) []int {
	result, stack := []int{}, []int{}
	length := 0
	for i := len(T) - 1; i >= 0; i-- {
		for length > 0 && T[stack[length-1]] <= T[i] {
			stack = stack[:length-1]
			length--
		}
		if length > 0 {
			result = append(result, stack[length-1]-i)
		} else {
			result = append(result, 0)
		}
		stack = append(stack, i)
		length++
	}
	n := len(result)
	for i := 0; i < int(n/2); i++ {
		result[i], result[n-i-1] = result[n-i-1], result[i]
	}
	return result
}