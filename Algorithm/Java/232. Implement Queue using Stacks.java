/*
* @Author: WuLC
* @Date:   2017-08-05 16:45:26
* @Last Modified by:   WuLC
* @Last Modified time: 2017-08-05 16:45:52
* @Email: liangchaowu5@gmail.com
*/


// use two queues
public class MyQueue {
    
    private Stack<Integer> in;
    private Stack<Integer> out;
    /** Initialize your data structure here. */
    public MyQueue() 
    {
        in = new Stack<Integer>();
        out = new Stack<Integer>();
    }
    
    /** Push element x to the back of queue. */
    public void push(int x) 
    {
        in.push(x);
    }
    
    /** Removes the element from in front of queue and returns that element. */
    public int pop() 
    {
        if(out.size() == 0)
        {
            while(in.size() > 0) 
                out.push(in.pop());
        }
        return out.pop();
    }
    
    /** Get the front element. */
    public int peek() 
    {
        if(out.size() == 0)
        {
            while(in.size() > 0) 
                out.push(in.pop());
        }
        return out.peek();
    }
    
    /** Returns whether the queue is empty. */
    public boolean empty() 
    {
        return in.size() + out.size() == 0;
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue obj = new MyQueue();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.peek();
 * boolean param_4 = obj.empty();
 */