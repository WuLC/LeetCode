/*
 * Created on Sun Jun 09 2019 18:53:47
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// stack
 func smallestSubsequence(text string) string {
	stack := []rune{}
	counter, stored := make(map[rune]int), make(map[rune]bool)
	for _, c := range text {
		counter[c]++
	}
	for _, c := range text {
		if val, ok := stored[c]; ok && val {
			counter[c]--
			continue
		}
		n := len(stack) - 1
		for len(stack) > 0 && stack[n] > c && counter[stack[n]] > 1 {
			counter[stack[n]]--
			stored[stack[n]] = false
			stack = stack[:n]
			n = len(stack) - 1
		}
		stack = append(stack, c)
        stored[c] = true
	}
	return string(stack)	
}