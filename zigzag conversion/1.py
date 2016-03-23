# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 15:34:44 2016

@author: xhong
"""

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        row_str = ['']*numRows
        step,row_ind = 1,0
        for char in s:
            row_str[row_ind] += char
            row_ind = row_ind + step
            if row_ind == 0 or row_ind == numRows-1:
                step = -step
        return ''.join(row_str)
            

solution = Solution()
s = 'PAYPALISHIRING'
numRows = 1
print(solution.convert(s,numRows))