/*
 * Created on Sun May 05 2019 17:15:28
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */


func isBoomerang(points [][]int) bool {
	p1, p2, p3 := points[0], points[1], points[2]
	return (p2[1] - p1[1]) * (p3[0] - p2[0]) != (p2[0] - p1[0]) * (p3[1] - p2[1])
}