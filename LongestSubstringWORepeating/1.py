# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 11:56:37 2016

@author: xhong
"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        str_temp = []
        str_now = []
        for i,char in enumerate(list(s)):
            if char in str_temp:
                str_temp = str_temp[(str_temp.index(char)+1):]
                str_temp.append(char)
            else:
                str_temp.append(char)
                if len(str_temp) > len(str_now):
                    str_now = str_temp
        return len(str_now)
        
solution = Solution()
s = 'dvdf'
print(solution.lengthOfLongestSubstring(s))

