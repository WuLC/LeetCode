/*
 * Created on Wed Feb 27 2019 20:54:22
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// record the number of lights at each row, column, left diagonal and right diagonal
// use hashmap instead of list to avoid memory limit exceeded

func gridIllumination(N int, lamps [][]int, queries [][]int) []int {
	row, col := make(map[int]int), make(map[int]int)
	left_diagonal, right_diagonal := make(map[int]int), make(map[int]int)
	source := make(map[int]map[int]int) // the value is also a map
	for _, v := range lamps {
		if _, ok := source[v[0]]; !ok {
			source[v[0]] = make(map[int]int)
		}
		source[v[0]][v[1]] = 1
		row[v[0]]++
		col[v[1]]++
		left_diagonal[v[0]+v[1]]++
		right_diagonal[v[0]-v[1]]++
	}

	result := []int{}
	for _, v := range queries {
		_, in_row := row[v[0]]
		_, in_col := col[v[1]]
		_, in_left_diagonal := left_diagonal[v[0]+v[1]]
		_, in_right_diagonal := right_diagonal[v[0]-v[1]]
		if (in_row && row[v[0]] > 0) ||
			(in_col && col[v[1]] > 0) ||
			(in_left_diagonal && left_diagonal[v[0]+v[1]] > 0) ||
			(in_right_diagonal && right_diagonal[v[0]-v[1]] > 0) {
			result = append(result, 1)
		} else {
			result = append(result, 0)
		}
		for i := v[0] - 1; i <= v[0]+1; i++ {
			for j := v[1] - 1; j <= v[1]+1; j++ {
				if val, ok := source[i]; ok {
					if _, ok := val[j]; ok {
						row[i]--
						col[j]--
						left_diagonal[i+j]--
						right_diagonal[i-j]--
					}
				}
			}
		}
	}
	return result
}