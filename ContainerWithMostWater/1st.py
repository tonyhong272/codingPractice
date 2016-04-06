class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = 0
        j = len(height) - 1
        maxWater = 0
        while i < j:
            maxWater1 = (j - i) * min(height[j], height[i])
            if maxWater1 > maxWater:
                maxWater = maxWater1
            if height[j] > height[i]:
                i += 1
            else:
                j -= 1
        return maxWater

solution = Solution()
height = [1,2,3]
print(solution.maxArea(height))
