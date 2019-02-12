/*
 * Created on Tue Feb 12 2019 20:23:13
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// chang Y to X
// greedy: when Y is odd, perform Y-1, else perform Y/2

func brokenCalc(X int, Y int) int {
    if X >= Y {
		return X-Y
	} else if (Y&1) == 1 {
		return 1 + brokenCalc(X, Y+1)
	} else {
		return 1 + brokenCalc(X, Y>>1)
	}
}