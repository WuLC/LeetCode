# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2017-03-06 14:35:20
# @Last modified by:   WuLC
# @Last Modified time: 2017-03-06 14:35:35
# @Email: liangchaowu5@gmail.com

import hashlib
class Codec:
    def __init__(self):
        self.mapping = {}
        self.baseUrl = 'http://tinyurl/'
        
    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        s = hashlib.sha384(longUrl).hexdigest()
        for i in xrange(1, len(s)):
            if s[:i] in self.mapping:
                continue
            self.mapping[s[:i]] = longUrl
            break
        return self.baseUrl+s[:i]
        

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        return self.mapping.get(shortUrl.strip().split('/')[-1], '')