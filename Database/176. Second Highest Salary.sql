/*
* @Author: LC
* @Date:   2017-03-19 23:08:39
* @Last Modified by:   WuLC
* @Last Modified time: 2017-03-19 23:38:26
*/

# pay attention that null should be returned when there is no appropriate result 


# method 1, use subquery to deal with NULL problem
SELECT(
SELECT DISTINCT Salary FROM Employee ORDER BY Salary DESC LIMIT  1,1
) AS SecondHighestSalary;


# method 2, max() will return a NULL if the value doesn't exist.
SELECT MAX(Salary) AS SecondHighestSalary FROM Employee 
WHERE Salary < (SELECT MAX(Salary) FROM Employee);