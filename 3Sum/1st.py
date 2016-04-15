class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        good_list = []
        nums.sort()
        for i in range(0, len(nums)):
            processed = {}
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, len(nums)):
                if nums[j] in processed:
                    new_list = ([nums[i], \
                                nums[processed[nums[j]]], nums[j]])
                    if new_list not in good_list:
                        good_list.append(new_list)
                        #print(i,j,nums[i], nums[j],new_list)
                else:
                    processed[(0-nums[i]-nums[j])] = j
                    #print processed
        return good_list

solution = Solution()
list = [1,2,-2,-1]
print(solution.threeSum(list))