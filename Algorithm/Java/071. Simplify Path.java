/**
* Author: WuLC
* Date:   2017-01-11 13:15:31
* Last modified by:   WuLC
* Last Modified time: 2017-01-11 13:15:44
* Email: liangchaowu5@gmail.com
*/

// stack
public class Solution 
{
    public String simplifyPath(String path) 
    {
        String result = "";
        Stack<String> stack = new Stack<String>();
        StringBuffer buffer = new StringBuffer();
        if (path.length() !=0 && path.charAt(path.length()-1) != '/') path += "/";
        for(int i=0; i<path.length(); i++)
        {
            char c = path.charAt(i);
            if(c == '/')
            {
                if (buffer.length() == 0) continue;
                
                String tmp = buffer.toString();
                if(!tmp.equals(".") && !tmp.equals("..") ) stack.push(tmp);
                else if(tmp.equals("..") && !stack.isEmpty()) stack.pop();
                buffer.delete(0, buffer.length());
            }
            else buffer.append(c);
        }
        if(stack.isEmpty()) return "/";
        while(!stack.isEmpty())
        {
            String tmp = stack.pop();
            result = "/"+tmp+result;
        }
        return result;
        
    }
}