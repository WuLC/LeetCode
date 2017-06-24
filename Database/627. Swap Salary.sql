/*
* @Author: WuLC
* @Date:   2017-06-24 10:36:39
* @Last Modified by:   WuLC
* @Last Modified time: 2017-06-24 10:37:02
*/

-- case statement
UPDAte salary set sex = 
(CASE 
WHEN sex='m' THEN 'f'
ELSE 'm'
END);
