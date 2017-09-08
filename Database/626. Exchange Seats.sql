/*
* @Author: WuLC
* @Date:   2017-09-09 00:06:56
* @Last Modified by:   WuLC
* @Last Modified time: 2017-09-09 00:09:24
*/


#For students with odd id, the new id is (id+1) after switch unless it is the last seat. 
#for students with even id, the new id is (id-1)
SELECT 
(CASE 
     WHEN MOD(id, 2) != 0 AND counts != id THEN id + 1
     WHEN MOD(id, 2) != 0 AND counts = id THEN id
     ELSE id -1
END) AS id, student 
FROM  seat, (SELECT COUNT(*) AS counts FROM seat) AS seat_counts
ORDER BY id ASC;