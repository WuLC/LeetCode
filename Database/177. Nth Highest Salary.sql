/*
* @Author: WuLC
* @Date:   2017-03-26 23:34:26
* @Last Modified by:   WuLC
* @Last Modified time: 2017-03-26 23:35:19
*/

# a variable need the be SET as N-1 instead of using it directly
# LIMIT offset, count
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
DECLARE M INT;
SET M=N-1;
  RETURN (
      # Write your MySQL query statement below.
      SELECT DISTINCT Salary FROM Employee ORDER BY Salary DESC LIMIT M, 1
  );
END