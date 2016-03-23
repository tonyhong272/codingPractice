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
        processed = {}
        for i,item in enumerate(nums):
            if (target - item) in processed:
                return [processed[target - item], i]
            else:
                processed[item] = i
        
nums = [0, 5, 1, 0]
target = 0
solution = Solution()
print(solution.twoSum(nums, target))