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
        for a in range(len(s)*2-1):
            i = a / 2.0
            new_length = self.checkLength(s,i,preLength)
            if new_length > preLength:
                preLength = int(new_length)
                if i == int(i):
                    longestStr = s[int(i-new_length/2) : int(i+new_length/2+1)]
                else:
                    longestStr = s[int(i+0.5-new_length/2) : int(i+0.5+new_length/2)]
        return longestStr
        
    def checkLength(self, s, i, preLength):
        if i==int(i) :
            i = int(i)
            n = preLength / 2
            while n>0 and i-n >= 0 and i+n <= len(s)-1 and s[i + n] == s[i - n]:
                n -= 1
            if n==0:
                m = preLength / 2
                while i-m >= 0 and i+m <= len(s)-1 and s[i + m] == s[i - m]:
                    m += 1
                return (m - 1) * 2 + 1
            else:
                return preLength            
        else:
            n = preLength / 2 - 0.5
            while n>0 and i-n >= 0 and i+n <= len(s)-1 and s[int(i + n)] == s[int(i - n)]:
                n -= 1
            if n == -0.5:
                m = preLength / 2 - 0.5
                while i-m >= 0 and i+m <= len(s)-1 and s[int(i + m)] == s[int(i - m)]:
                    m += 1
                return (m - 0.5) * 2
            else:
                return preLength            

solution = Solution()
s = 'a'
print(solution.longestPalindrome(s))