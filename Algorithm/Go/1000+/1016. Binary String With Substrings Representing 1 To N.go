/*
 * Created on Fri Apr 12 2019 22:29:26
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// set

func queryString(S string, N int) bool {
    result, next := make(map[int]bool), make(map[int]bool)
    result[0] = true
    next[0] = true
    for _, c := range S {
        bit := int(c - '0')
        curr := make(map[int]bool)
        for k, v := range next {
            curr[k] = v
            delete(next, k)
        }
        next[0] = true
        for k := range curr {
            val := (k << 1) + bit
            if val <= N {
                result[val] = true
                next[val] = true
            }
        }
        if len(result) == N + 1 {
            return true
        }
    }
    return false
}