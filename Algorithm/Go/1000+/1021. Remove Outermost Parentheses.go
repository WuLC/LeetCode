/*
 * Created on Tue Apr 09 2019 10:53:1
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

func removeOuterParentheses(S string) string {
	result, stack := "", []int{}
	for i, c := range S {
		if c == '(' {
			stack = append(stack, i)
		} else {
			idx := stack[len(stack) - 1]
			stack = stack[:len(stack) - 1]
			if len(stack) == 0 {
				result += S[idx + 1 : i]
			}
		}
	}
	return result
}