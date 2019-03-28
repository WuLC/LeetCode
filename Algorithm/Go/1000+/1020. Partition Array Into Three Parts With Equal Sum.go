/*
 * Created on Thu Mar 28 2019 23:39:19
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

func canThreePartsEqualSum(A []int) bool {
	s := 0
	for _, num := range A {
		s += num
	} 
	if s % 3 != 0 {
		return false
	}
	ave := s/3
	count, tmp := 0, 0
	for _, num := range A {
		if tmp == ave {
			count++
			tmp = 0
		}
		tmp += num
	}
	if tmp == ave {
		count++
	}
	return count == 3
}
