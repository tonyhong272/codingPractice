class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        good_list = []
        nums.sort()
        for i in range(0, len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, k = i + 1, len(nums) - 1
            while l < k:
                if nums[l] + nums[k] + nums[i] == 0:
                    if not(k < len(nums) - 1 and nums[k] == nums[k+1]):
                        good_list.append([nums[i], nums[l], nums[k]])
                    l += 1
                    if nums[l] == nums[l-1]:
                        l += 1
                    k -= 1
                    if nums[k] == nums[k+1]:
                        k -= 1
                elif nums[l] + nums[k] + nums[i] < 0:
                    l += 1
                    if nums[l] == nums[l - 1]:
                        l += 1
                elif nums[l] + nums[k] + nums[i] > 0:
                    k -= 1
                    if nums[k] == nums[k + 1]:
                        k -= 1
        return good_list

solution = Solution()
list = [-2,0,3,-1,4,0,3,4,1,1,1,-3,-5,4,0]
print(solution.threeSum(list))