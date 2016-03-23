
"""
Created on Mon Mar 21 16:17:15 2016

@author: xhong
"""
import math


class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        if x == 0:
            return True

        order = int(math.log10(x))
        while order >= 0:
            last = x % 10
            x -= last * (10 ** order)
            x /= 10
            order -= 2
        return x == 0

solution = Solution()
x = 10
print(solution.isPalindrome(x))
