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
            new_string = self.checkString(s,i,preLength)
#            print(new_string)
            if len(new_string) > preLength:
                preLength = int(len(new_string))
                longestStr = new_string
        return longestStr
        
    def checkString(self, s, i, preLength):
        if i==int(i) :
            i = int(i)
            n = preLength / 2
            if i-n == 0:
                s1,s2 = s[(i - n) : (i + n + 1)] , s[(i + n) ::-1]
            else:
                s1,s2 = s[(i - n) : (i + n + 1)] , s[(i + n) : (i - n - 1):-1]
            while i-n >= 0 and i+n <= len(s)-1 and s1== s2:
                n += 1
                if i-n == 0:
                    s1,s2 = s[(i - n) : (i + n + 1)] , s[(i + n) ::-1]
                elif i-n > 0:
                    s1,s2 = s[(i - n) : (i + n + 1)] , s[(i + n) : (i - n - 1):-1]
#                print(i,n,s1,s2)
                if s1 != s2 or i-n < 0 or i + n >= len(s):
                    n -= 1
                    s1 = s[(i - n) : (i + n + 1)]
                    return s1
            return []
        else:
            n = preLength / 2 + 0.5
            if i-n == 0:
                s1,s2 = s[int(i - n) : int(i + n+1)] , s[int(i + n) ::-1]
            else:
                s1,s2 = s[int(i - n) : int(i + n+1)] , s[int(i + n) : int(i - n - 1):-1]
            while i-n >= 0 and i+n <= len(s)-1 and s1== s2:
                n += 1
                if i-n == 0:
                    s1,s2 = s[int(i - n) : int(i + n+1)] , s[int(i + n) ::-1]
                elif i-n > 0:
                    s1,s2 = s[int(i - n) : int(i + n+1)] , s[int(i + n) : int(i - n-1):-1]

                if s1 != s2 or i-n < 0 or i + n >= len(s):
                    n -= 1
                    s1 = s[int(i - n) : int(i + n+1)]
                    return s1
            return []
solution = Solution()
s = "tattarrattat"
print(solution.longestPalindrome(s))