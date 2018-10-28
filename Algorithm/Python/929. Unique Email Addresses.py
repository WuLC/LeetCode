# -*- coding: utf-8 -*-
# Created on Sun Oct 28 2018 17:4:17
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# simple solution
class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        def format(s):
            result = []
            for c in s:
                if c == '+':
                    break
                elif c == '.':
                    continue
                else:
                    result.append(c)
            return ''.join(result)
        uniuqe_emails = set()
        for email in emails:
            name, domain = email.split('@')
            uniuqe_emails.add(format(name) + '@' + domain)
        return len(uniuqe_emails)