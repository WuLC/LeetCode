/*
 * Created on Sat Jan 05 2019 16:50:16
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// recursive
func numsSameConsecDiff(N int, K int) []int {
	if N == 1 {
		return []int{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
	} else {
		result := []int{}
		for i := 1; i < 10; i++ {
			for _, strNum := range generate(strconv.Itoa(i), N, K) {
				num, _ := strconv.Atoi(strNum)
				result = append(result, num)
			}
		}
		return result
	}
}

func generate(digit string, N int, K int) []string {
	subResult := []string{}
	if N == 1 {
		subResult = append(subResult, digit)
	} else {
		digitValue, _ := strconv.Atoi(digit)
		if digitValue-K >= 0 {
			for _, sub := range generate(strconv.Itoa(digitValue-K), N-1, K) {
				buffer := bytes.NewBufferString(digit)
				buffer.WriteString(sub)
				subResult = append(subResult, buffer.String())
			}
		}
		if K != 0 && digitValue+K < 10 {
			for _, sub := range generate(strconv.Itoa(digitValue+K), N-1, K) {
				buffer := bytes.NewBufferString(digit)
				buffer.WriteString(sub)
				subResult = append(subResult, buffer.String())
			}
		}
	}
	return subResult
}