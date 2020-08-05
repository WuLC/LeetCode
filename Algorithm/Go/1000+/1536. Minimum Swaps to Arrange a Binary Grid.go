func minSwaps(grid [][]int) int {
	zeroCnts := []int{}
	for _, arr := range grid {
		zeroCnts = append(zeroCnts, getZeroCnt(arr))
	}

	result, n := 0, len(grid)
	for i, _ := range zeroCnts {
		if zeroCnts[i] >= n-i-1 {
			continue
		} else {
			j := i + 1
			for j < n && zeroCnts[j] < n-i-1 {
				j++
			}
			if j == n {
				return -1
			} else {
				result += j - i
				for j > i {
					zeroCnts[j], zeroCnts[j-1] = zeroCnts[j-1], zeroCnts[j]
					j--
				}
			}
		}
	}
	return result
}

func getZeroCnt(row []int) int {
	result, i := 0, len(row)-1
	for i >= 0 {
		if row[i] == 0 {
			i--
			result++
		} else {
			break
		}
	}
	return result
}