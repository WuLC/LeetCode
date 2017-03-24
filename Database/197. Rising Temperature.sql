/*
* @Author: WuLC
* @Date:   2017-03-25 00:17:20
* @Last Modified by:   WuLC
* @Last Modified time: 2017-03-25 00:19:46
*/

# Inner join on the same table, two ways to implement it 
SELECT w1.Id FROM Weather w1, Weather w2 WHERE w1.Temperature > w2.Temperature AND SUBDATE(w1.Date,1) = w2.Date;
SELECT w1.Id FROM Weather w1 JOIN Weather w2 ON w1.Temperature > w2.Temperature AND SUBDATE(w1.Date,1) = w2.Date;