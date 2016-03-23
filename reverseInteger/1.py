# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 15:34:44 2016

@author: xhong
"""

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x==0:
            return 0
        str_x = str(abs(x))
        sign = x/abs(x)
        str_x = str_x[::-1]
        if int(str_x) < 2147483647:
            result = sign*int(str_x)
        else:
            result = 0
        return result

solution = Solution()
x = -123
print(solution.reverse(x))