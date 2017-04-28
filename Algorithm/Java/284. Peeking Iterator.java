/**
* Author: WuLC
* Date:   2017-04-28 11:37:12
* Last modified by:   WuLC
* Last Modified time: 2017-04-28 11:38:06
* Email: liangchaowu5@gmail.com
*/


// Java Iterator interface reference:
// https://docs.oracle.com/javase/8/docs/api/java/util/Iterator.html


// use ArrayList as a queue
class PeekingIterator implements Iterator<Integer> 
{
    private List<Integer> queue;
    public PeekingIterator(Iterator<Integer> iterator) 
    {
        queue = new ArrayList<Integer>();
        while(iterator.hasNext())
        {
            queue.add(iterator.next());
        }
    }

    // Returns the next element in the iteration without advancing the iterator.
    public Integer peek() 
    {
        if (queue.size() > 0) return queue.get(0);
        else return null;
    }

    // hasNext() and next() should behave the same as in the Iterator interface.
    // Override them if needed.
    @Override
    public Integer next() 
    {
        Integer head = queue.get(0);
        queue.remove(0);
        return head;
    }

    @Override
    public boolean hasNext() 
    {
        return queue.size() > 0;
        
    }
}