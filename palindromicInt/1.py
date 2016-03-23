# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 16:17:15 2016

@author: xhong
"""
import math
class Solution(object):
    def getNumber(self, x, digit):
        return (x - x / 10**(digit) *10**digit)/10**(digit-1)

    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0: return False
        if x == 0: return True
        length = int(math.log10(x))+1
        digit = 0
        while self.getNumber(x, digit) == self.getNumber(x, length+1 - digit):
            digit += 1
            if digit > (length+1)/2:
                return True
        return False
        
solution = Solution()
x=1012101
print(solution.isPalindrome(x))