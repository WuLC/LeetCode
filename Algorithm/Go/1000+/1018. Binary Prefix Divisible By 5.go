/*
 * Created on Sun Apr 07 2019 20:57:3
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */


func prefixesDivBy5(A []int) []bool {
	result := []bool{}
	curr := 0
	for _, num := range A {
		curr = (curr * 2 + num) % 5
		if curr == 0 {
			result = append(result, true)
		} else {
			result = append(result, false)
		}
	}
	return result
}