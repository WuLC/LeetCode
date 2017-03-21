/*
* @Author: WuLC
* @Date:   2017-03-21 22:10:18
* @Last Modified by:   WuLC
* @Last Modified time: 2017-03-21 22:10:33
*/

# subquery
SELECT Name AS Customers FROM Customers WHERE Id NOT IN (SELECT DISTINCT CustomerId FROM Orders);