# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 10:01:28 2016

@author: xhong
"""
# inefficient because character-wise comparison is slow and high overhead.

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        preLength = 1
        longestStr = s[0]
        for i in range(len(s)):
            new_string = self.checkString(s,i,preLength)
            if len(new_string) > preLength:
                preLength = int(len(new_string))
                longestStr = new_string
        return longestStr
        
    def checkString(self, s, i, preLength):
        n = preLength / 2
        longStr = []
        while i-n>=0 and i+n <= len(s)-1 and s[i-n:i+n+1]==s[i-n : i+n+1][::-1]:
            n += 1
            if i-n<0 or i+n>=len(s) or s[i-n:i+n+1]!=s[i-n : i+n+1][::-1] :
                n-=1
                longStr = s[(i-n):(i+n+1)]
                break
        while i-n>=0 and i+n+1<= len(s)-1 and s[i-n:i+n+2]==s[i-n: i+n+2][::-1]:
            n += 1
            if i-n<0 or i+n+1>=len(s) or s[i-n:i+n+2]!=s[i-n : i+n+2][::-1]:
                n-=1
                longStr = s[i-n:i+n+2]
                break
        return longStr
solution = Solution()
s = "bb"
print(solution.longestPalindrome(s))