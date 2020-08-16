func threeConsecutiveOdds(arr []int) bool {
	cnt := 0
	for _, num := range arr {
		if num&1 > 0 {
			cnt++
			if cnt == 3 {
				return true
			}
		} else {
			cnt = 0
		}
	}
	return false
}