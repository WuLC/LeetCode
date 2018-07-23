/*
 * Created on Mon Jul 23 2018 16:29:40
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

--group by with having clause
SELECT class FROM courses GROUP BY class HAVING COUNT(DISTINCT student) >= 5;