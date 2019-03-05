/*
 * Created on Mon Mar 04 2019 20:56:21
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// simple solution, be careful of the problem of MLE

// MLE solution
func commonChars(A []string) []string {
	counter := []map[string]int{}
	for i, s := range A {
		tmp := make(map[string]int)
		for _, c := range s {
			tmp[c]++
		}
		counter = append(counter, tmp)
	}
	result := []string{}
	for k, v := range counter[0] {
		for i := 1; i < len(counter); i++ {
			if v < counter[i][k] {
				v = counter[i][k]
			}
		}
		for v > 0 {
			result = append(result, k)
		}
	}
	return result
}

// AC solution
func min(a, b int) int {
	if a < b {
		return a
	} else {
		return b
	}
}

func commonChars(A []string) []string {
	curr := make(map[string]int)
	for i, s := range A {
		tmp := make(map[string]int)
		for _, c := range s {
			tmp[string(c)]++
		}
		if i == 0 {
			curr = tmp
		} else {
			for k, v := range curr {
				if val, present := tmp[k]; present {
					curr[k] = min(v, val)
				} else {
					delete(curr, k)
				}
			}
		}
	}
	result := []string{}
	for k, v := range curr {
		for v > 0 {
			result = append(result, k)
			v--
		}
	}
	return result
}