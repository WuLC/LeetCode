class Solution(object):
    def findWordsContaining(self, words, x):
        """
        :type words: List[str]
        :type x: str
        :rtype: List[int]
        """

        def contain(word, c):
            for char in word:
                if c == char:
                    return True
            return False
    
        return [i for i in range(len(words)) if contain(words[i], x)]
        