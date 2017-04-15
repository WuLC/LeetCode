/**
* Author: WuLC
* Date:   2017-04-15 23:58:19
* Last modified by:   WuLC
* Last Modified time: 2017-04-15 23:58:56
* Email: liangchaowu5@gmail.com
*/


// use hashmap to store children
class TrieNode
{
    public char word = ' ';
    public Map<Character, TrieNode> next = new HashMap<Character, TrieNode>();
    boolean isWord = false;
}
    
public class Trie {

    /** Initialize your data structure here. */
    private TrieNode root = null;
    
    public Trie() 
    {
        root = new TrieNode();
    }
    
    /** Inserts a word into the trie. */
    public void insert(String word) 
    {
        TrieNode curr = root;
        char[] chars = word.toCharArray();
        for(int i=0; i < chars.length; i++)
        {
            if (!curr.next.containsKey(chars[i]))
            {
                curr.next.put(chars[i], new TrieNode());
            }
            curr = curr.next.get(chars[i]);
            curr.word = chars[i];
        }
        curr.isWord = true;
    }
    
    /** Returns if the word is in the trie. */
    public boolean search(String word) 
    {
        TrieNode curr = root;
        char[] chars = word.toCharArray();
        for(int i=0; i < chars.length; i++)
        {
            if (curr.next.containsKey(chars[i])) curr = curr.next.get(chars[i]);
            else return false;
        }
        if (curr.isWord) return true;
        else return false;
    }
    
    /** Returns if there is any word in the trie that starts with the given prefix. */
    public boolean startsWith(String prefix) 
    {
        TrieNode curr = root;
        char[] chars = prefix.toCharArray();
        for(int i=0; i < chars.length; i++)
        {
            if (curr.next.containsKey(chars[i])) curr = curr.next.get(chars[i]);
            else return false;
        }
        return true;
    }
}

/**
 * Your Trie object will be instantiated and called as such:
 * Trie obj = new Trie();
 * obj.insert(word);
 * boolean param_2 = obj.search(word);
 * boolean param_3 = obj.startsWith(prefix);
 */