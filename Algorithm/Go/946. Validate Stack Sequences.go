/*
 * Created on Wed Nov 28 2018 9:58:52
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// implement stack with slice
func validateStackSequences(pushed []int, popped []int) bool {
	var stack []int
	p1, p2 := 0, 0
	for p1 < len(pushed) && p2 < len(popped) {
		if pushed[p1] == popped[p2] {
			p1++
			p2++
		} else if len(stack) > 0 && stack[len(stack)-1] == popped[p2] {
			stack = stack[:len(stack)-1]
			p2++
		} else {
			for p1 < len(pushed) && pushed[p1] != popped[p2] {
				stack = append(stack, pushed[p1])
				p1++
			}
		}
	}
	for p2 < len(popped) && len(stack) > 0 && stack[len(stack)-1] == popped[p2] {
		p2++
		stack = stack[:len(stack)-1]
	}
	return p2 == len(popped)
}