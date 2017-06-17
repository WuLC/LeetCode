/*
* @Author: LC
* @Date:   2017-06-17 08:32:54
* @Last Modified by:   LC
* @Last Modified time: 2017-06-17 08:33:06
*/
# Write your MySQL query statement below
SELECT * FROM cinema WHERE id%2 = 1 AND description != "boring" ORDER BY rating DESC;