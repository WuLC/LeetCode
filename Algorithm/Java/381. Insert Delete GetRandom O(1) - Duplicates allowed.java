/**
* Author: WuLC
* Date:   2017-04-20 09:57:28
* Last modified by:   WuLC
* Last Modified time: 2017-04-20 10:03:14
* Email: liangchaowu5@gmail.com
*/


// use an arraylist to store all elements and a hashmap to store indices of same element
public class RandomizedCollection 
{
    private ArrayList<Integer> numList;
    private HashMap<Integer, ArrayList<Integer>> indexMap;

    /** Initialize your data structure here. */
    public RandomizedCollection() 
    {
        numList = new ArrayList<Integer>();
        indexMap = new HashMap<Integer, ArrayList<Integer>>();
    }
    
    /** Inserts a value to the collection. Returns true if the collection did not already contain the specified element. */
    public boolean insert(int val) 
    {
        numList.add(val);
        if(!indexMap.containsKey(val)) 
        {
            indexMap.put(val, new ArrayList<Integer>());
            indexMap.get(val).add(numList.size()-1);
            return true;
        }
        else
        {
            indexMap.get(val).add(numList.size()-1);
            return false;
        }
    }
    
    /** Removes a value from the collection. Returns true if the collection contained the specified element. */
    public boolean remove(int val) 
    {
        if (indexMap.containsKey(val) && indexMap.get(val).size() > 0)
        {
            ArrayList<Integer> tmp = indexMap.get(val);
            int removeIndex = tmp.get(tmp.size()-1);
            tmp.remove(tmp.size()-1);
            
            if (removeIndex != numList.size() - 1)
            {
                int replaceInt = numList.get(numList.size()-1);
                numList.set(removeIndex, replaceInt);
                tmp = indexMap.get(replaceInt);
                for(int i=tmp.size()-1; i >= 0; i--)
                {
                    if (tmp.get(i) == numList.size()-1)
                    {
                        tmp.set(i, removeIndex);
                        break;
                    }
                }
            }
            numList.remove(numList.size()-1);
            return true;
        }
        else return false;
    }
    
    /** Get a random element from the collection. */
    public int getRandom() 
    { 
        int idx = (int)(Math.random()*numList.size());
        return numList.get(idx);
    }
}

