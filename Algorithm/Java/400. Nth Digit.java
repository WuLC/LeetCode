/*
* @Author: WuLC
* @Date:   2017-09-10 08:57:52
* @Last Modified by:   WuLC
* @Last Modified time: 2017-09-10 15:03:48
*/


// be careful of overflow, use long instead of int

class Solution 
{
    public int findNthDigit(int n) 
    {
        int i = 1;
        while(true)
        {
            long tmp = (long)Math.pow(10, i-1) * 9 * i;
            if (n > tmp)
            {
                n -= tmp;
                i += 1;
            }
            else
            {
                int c = (n - 1) / i;
                int num = (int)Math.pow(10, i - 1) + c;
                return String.valueOf(num).charAt((n-1) % i) - '0';
            }
        }
        
    }
}

// more concise
class Solution 
{
	public int findNthDigit(int n) 
	{
		int len = 1;
		long count = 9;
		int start = 1;

		while (n > len * count) 
		{
			n -= len * count;
			len += 1;
			count *= 10;
			start *= 10;
		}

		start += (n - 1) / len;
		String s = Integer.toString(start);
		return Character.getNumericValue(s.charAt((n - 1) % len));
	}
}