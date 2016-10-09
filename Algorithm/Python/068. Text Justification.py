# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-05-12 09:33:08
# @Last modified by:   WuLC
# @Last Modified time: 2016-05-12 10:38:40
# @Email: liangchaowu5@gmail.com

# Notice !!! 
# there exists at least one space between two words
class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        if len(words) == 0:
            return None
        length = map(lambda x:len(x),words)
        count = length[0]+1
        begin = 0
        result = []
        for i in xrange(len(words)):
            if i == len(words)-1: # last line
                """
                extra = maxWidth - sum(length[begin:i+1])-(i-begin)
                result.append(' '.join(words[begin:i+1])+' '*extra)
                break
                # comment blcok is equal to the following four lines
                """
                word_num = i - begin + 1
                extra = maxWidth - count + 1
                result.append(' '.join(words[begin:i+1])+' '*extra)
                break
            if count + length[i+1] > maxWidth:
                word_num = i - begin + 1
                extra = maxWidth - count + word_num # all spaces should be placed between words
                # the above line is equal to
                # extra = maxWidth - sum(length[begin:i+1])
                if word_num == 1:
                   result.append(words[begin]+' '*extra) 
                else:
                    ave, extra=divmod(extra,word_num-1)
                    tmp = map(lambda x:x+' '*ave, words[begin:i])
                    tmp.append(words[i])
                    for j in xrange(extra):
                        tmp[j] += ' '
                    result.append(''.join(tmp))
                count = length[i+1]+1
                begin = i + 1
            else:
                count+=length[i+1]+1
        return result        
                    
