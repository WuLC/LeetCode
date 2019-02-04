/*
 * Created on Mon Feb 04 2019 12:11:56
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

 /**
 * Definition for an interval.
 * type Interval struct {
 *	   Start int
 *	   End   int
 * }
 */

 import "math"

 func intervalIntersection(A []Interval, B []Interval) []Interval {
	 result := []Interval{}
	 p1, p2 := 0, 0
	 for p1<len(A) && p2<len(B) {
		 if A[p1].End < B[p2].Start {
			 p1++
		 } else if A[p1].Start > B[p2].End {
			 p2++
		 } else {
			 s := int(math.Max(float64(A[p1].Start), float64(B[p2].Start)))
			 e := int(math.Min(float64(A[p1].End), float64(B[p2].End)))
			 result = append(result, Interval{s, e})
			 if A[p1].End < B[p2].End {
				 p1++
			 } else {
				 p2++
			 }
		 }
	 }
	 return result
 }