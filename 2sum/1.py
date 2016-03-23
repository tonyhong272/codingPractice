# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 12:21:27 2016

@author: xhong
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j] == target:
                    return (i,j)
        
nums = [3, 5, 6, 10]
target = 9
solution = Solution()  
print(solution.twoSum(nums, target))