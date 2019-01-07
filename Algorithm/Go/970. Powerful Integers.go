/*
 * Created on Mon Jan 07 2019 19:51:23
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// generate candidate for x^i and y^j seperately and add them up
func powerfulIntegers(x int, y int, bound int) []int {
	candidateX, candidateY := []int{1}, []int{1}
	count := 1
	tmpX, tmpY := x, y
	for (x != 1 && tmpX < bound) || (y != 1 && tmpY < bound) {
		count++
		if x != 1 && tmpX < bound {
			candidateX = append(candidateX, tmpX)
			tmpX = int(math.Pow(float64(x), float64(count)))
		}
		if y != 1 && tmpY < bound {
			candidateY = append(candidateY, tmpY)
			tmpY = int(math.Pow(float64(y), float64(count)))
		}
	}
	nums := make(map[int]bool)
	for i := 0; i < len(candidateX); i++ {
		for j := 0; j < len(candidateY); j++ {
			sum := candidateX[i] + candidateY[j]
			if sum > bound {
				break
			}
			if _, found := nums[sum]; !found {
				nums[sum] = true
			}
		}
	}
	result := []int{}
	for num := range nums {
		result = append(result, num)
	}
	return result
}