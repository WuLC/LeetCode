/*
 * Created on Thu Feb 28 2019 9:15:33
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// simple solution
func numRookCaptures(board [][]byte) int {
	result := 0
	for i := 0; i < 8; i++ {
		for j := 0; j < 8; j++ {
			if board[i][j] == 'R' {
				directions := [][]int{{-1, 0}, {1, 0}, {0, -1}, {0, 1}}
				for _, d := range directions {
					ni, nj := i, j
					for ni+d[0] >= 0 && ni+d[0] < 8 && nj+d[1] >= 0 && nj+d[1] < 8 {
						ni += d[0]
						nj += d[1]
						if board[ni][nj] == 'B' {
							break
						} else if board[ni][nj] == 'p' {
							result++
							break
						}
					}
				}
				return result
			}
		}
	}
	return result
}